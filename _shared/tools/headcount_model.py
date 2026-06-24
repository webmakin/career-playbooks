#!/usr/bin/env python3
"""
headcount_model.py — Engineering org cost, ramp time, retention, hiring funnel.

Models:
  - Engineering headcount cost (base + bonus + equity + benefits + on-costs).
  - Ramp time (months to full productivity per level).
  - Retention risk (probability of leaving per level per quarter).
  - Hiring funnel (reqs -> offers -> accept -> ramp).
  - Org-shape cost (cost ratio Director:EM:IC).

Usage:
  python3 headcount_model.py --fixture
  python3 headcount_model.py --org 250 --director-ratio 1:10
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass
class EngineerLevel:
    name: str           # e.g. "IC2", "IC3 (Senior)", "IC4 (Staff)"
    base_salary: float  # USD
    bonus_pct: float    # 0.0-1.0
    equity_pct: float   # 0.0-1.0
    benefits_pct: float # 0.0-1.0
    on_cost_pct: float  # 0.0-1.0 (overhead, facilities, etc.)
    ramp_months: int    # months to full productivity
    retention_q: float  # probability of leaving per quarter (0.0-1.0)


LEVELS = {
    "IC1": EngineerLevel("IC1 (Junior)",         130_000, 0.10, 0.05, 0.20, 0.15, 3, 0.10),
    "IC2": EngineerLevel("IC2 (Mid)",            165_000, 0.15, 0.10, 0.20, 0.15, 4, 0.06),
    "IC3": EngineerLevel("IC3 (Senior)",         205_000, 0.20, 0.20, 0.20, 0.15, 6, 0.04),
    "IC4": EngineerLevel("IC4 (Staff)",          255_000, 0.25, 0.35, 0.20, 0.15, 9, 0.03),
    "IC5": EngineerLevel("IC5 (Principal)",      310_000, 0.30, 0.50, 0.20, 0.15, 12, 0.025),
    "IC6": EngineerLevel("IC6 (Distinguished)",  380_000, 0.35, 0.70, 0.20, 0.15, 18, 0.02),
    "EM":  EngineerLevel("EM",                   225_000, 0.20, 0.25, 0.20, 0.15, 6, 0.04),
    "DIR": EngineerLevel("Director",             290_000, 0.30, 0.50, 0.20, 0.15, 9, 0.025),
}


def total_comp(level: EngineerLevel) -> float:
    """Total annual cost of an engineer at a given level (base + bonus + equity + benefits + on-costs)."""
    base = level.base_salary
    bonus = base * level.bonus_pct
    equity = base * level.equity_pct
    benefits = base * level.benefits_pct
    on_costs = base * level.on_cost_pct
    return base + bonus + equity + benefits + on_costs


def ramp_loss(level: EngineerLevel, months_in_role: int) -> float:
    """
    Productivity loss during ramp. Returns fraction of full productivity
    (0.0 = 0% productive, 1.0 = 100% productive).
    Linear ramp over `ramp_months` months, then 100%.
    """
    if months_in_role >= level.ramp_months:
        return 1.0
    return months_in_role / level.ramp_months


def annual_attrition(level: EngineerLevel) -> float:
    """Convert quarterly retention risk to annual attrition rate."""
    return 1.0 - (1.0 - level.retention_q) ** 4


def org_shape_cost(levels: dict[str, int]) -> dict:
    """
    Given a mix of {level: count}, return total annual cost and per-engineer cost.
    """
    if not levels:
        return {"total": 0, "per_engineer": 0, "count": 0}
    total = 0.0
    count = 0
    for level_name, n in levels.items():
        if level_name not in LEVELS:
            print(f"headcount_model: unknown level {level_name!r}", file=sys.stderr)
            continue
        total += total_comp(LEVELS[level_name]) * n
        count += n
    return {
        "total": total,
        "per_engineer": total / count if count else 0,
        "count": count,
    }


def hiring_funnel(reqs: int, offer_rate: float, accept_rate: float) -> dict:
    """
    Model the hiring funnel: reqs -> offers -> accept.
    offer_rate: fraction of reqs that result in an offer.
    accept_rate: fraction of offers that result in an accepted offer.
    """
    offers = reqs * offer_rate
    accepts = offers * accept_rate
    return {
        "reqs": reqs,
        "offers": offers,
        "accepts": accepts,
        "offer_rate": offer_rate,
        "accept_rate": accept_rate,
        "fill_rate": accepts / reqs if reqs else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Engineering org cost, retention, hiring funnel modeling.")
    parser.add_argument("--fixture", action="store_true", help="Run the example fixture.")
    parser.add_argument("--org", type=int, help="Total engineering headcount.")
    parser.add_argument("--director-ratio", type=str, help="Director:IC ratio (e.g. '1:10').")
    args = parser.parse_args()

    if args.fixture:
        # Example: 250 engineers with a 1:10 Director:IC ratio
        # Default mix: 40% IC2, 30% IC3, 15% IC4, 5% IC5, 10% EM
        # 250 / 11 = ~23 Directors (1:10)
        total_eng = 250
        n_dir = 23
        n_em = int(0.10 * total_eng)  # ~25 EMs
        n_ic2 = int(0.40 * (total_eng - n_dir - n_em))  # ~80
        n_ic3 = int(0.30 * (total_eng - n_dir - n_em))  # ~60
        n_ic4 = int(0.15 * (total_eng - n_dir - n_em))  # ~30
        n_ic5 = int(0.10 * (total_eng - n_dir - n_em))  # ~20
        n_ic1 = total_eng - n_dir - n_em - n_ic2 - n_ic3 - n_ic4 - n_ic5  # ~12
        levels = {
            "DIR": n_dir,
            "EM":  n_em,
            "IC1": n_ic1,
            "IC2": n_ic2,
            "IC3": n_ic3,
            "IC4": n_ic4,
            "IC5": n_ic5,
        }
        result = org_shape_cost(levels)
        print("=== Engineering Org Cost (250 engineers, 1:10 Director:IC) ===\n")
        for level_name, n in levels.items():
            level = LEVELS[level_name]
            cost = total_comp(level)
            print(f"  {level.name:<25} {n:>4} x ${cost:>10,.0f} = ${cost * n:>14,.0f}")
        print(f"\n  Total headcount:   {result['count']}")
        print(f"  Total annual cost: ${result['total']:,.0f}")
        print(f"  Per engineer:      ${result['per_engineer']:,.0f}")
        # Retention
        print("\n=== Annual Attrition ===\n")
        for level_name in levels:
            level = LEVELS[level_name]
            attr = annual_attrition(level)
            print(f"  {level.name:<25} {attr * 100:.1f}% / year")
        # Hiring funnel
        print("\n=== Hiring Funnel (50 open reqs) ===\n")
        funnel = hiring_funnel(50, offer_rate=0.40, accept_rate=0.70)
        print(f"  Reqs:    {funnel['reqs']}")
        print(f"  Offers:  {funnel['offers']:.1f}  (offer rate: {funnel['offer_rate']:.0%})")
        print(f"  Accepts: {funnel['accepts']:.1f}  (accept rate: {funnel['accept_rate']:.0%})")
        print(f"  Fill rate: {funnel['fill_rate']:.0%}")
        return 0

    if args.org and args.director_ratio:
        # Parse Director:IC ratio
        try:
            d, i = args.director_ratio.split(":")
            d, i = int(d), int(i)
        except (ValueError, AttributeError):
            print("headcount_model: --director-ratio must be in form '1:10'", file=sys.stderr)
            return 1
        n_dir = max(1, args.org // (d + i))
        levels = {
            "DIR": n_dir,
            "EM":  int(0.10 * args.org),
            "IC3": int(0.40 * args.org),
            "IC4": int(0.10 * args.org),
        }
        result = org_shape_cost(levels)
        print(f"Total annual cost: ${result['total']:,.0f}")
        print(f"Per engineer:      ${result['per_engineer']:,.0f}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
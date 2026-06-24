#!/usr/bin/env python3
"""
deployment_economics.py — FDE deployment cost, time-to-deployment, customer LTV.

Models:
  - Customer deployment cost (engineering + customer success + infrastructure).
  - Time-to-deployment (Discovery -> Production in weeks).
  - Customer LTV vs. deployment cost (the FDE ROI calculation).
  - Customer retention (renewal rate by FDE vs. no FDE).

Usage:
  python3 deployment_economics.py --fixture
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass
class DeploymentPhase:
    name: str             # e.g. "Discovery", "Design"
    weeks: int            # typical weeks for this phase
    fde_pct: float        # FDE allocation (0.0-1.0)
    other_cost: float     # non-FDE cost per week (other eng, infra, etc.)


PHASES = [
    DeploymentPhase("Discovery",  2, 1.0, 2_000),  # 2 weeks, FDE full-time, +$2K/wk other
    DeploymentPhase("Design",     3, 1.0, 3_000),
    DeploymentPhase("Pilot",      4, 0.8, 5_000),
    DeploymentPhase("Production", 3, 0.5, 8_000),
    DeploymentPhase("Operate",    4, 0.2, 6_000),  # first 4 weeks of operation
    DeploymentPhase("Hand-off",   2, 0.3, 3_000),
]


def fde_loaded_cost(weeks: int, fde_weekly: float = 6_000) -> float:
    """FDE loaded cost: $6K/week (loaded = base + bonus + equity + benefits + on-costs)."""
    return weeks * fde_weekly


def deployment_cost(fde_weekly: float = 6_000) -> dict:
    """
    Total deployment cost (FDE + other) across all 6 phases.
    """
    total_weeks = 0
    total_cost = 0.0
    phase_costs = []
    for phase in PHASES:
        fde_cost = phase.weeks * phase.fde_pct * fde_weekly
        other_cost = phase.weeks * phase.other_cost
        phase_cost = fde_cost + other_cost
        phase_costs.append({
            "name": phase.name,
            "weeks": phase.weeks,
            "fde_cost": fde_cost,
            "other_cost": other_cost,
            "total": phase_cost,
        })
        total_weeks += phase.weeks
        total_cost += phase_cost
    return {
        "total_weeks": total_weeks,
        "total_cost": total_cost,
        "total": total_cost,  # alias for symmetry
        "phases": phase_costs,
    }


def time_to_deployment() -> dict:
    """Time-to-deployment (Discovery -> Production) in weeks."""
    phases = [p for p in PHASES if p.name in ("Discovery", "Design", "Pilot", "Production")]
    total = sum(p.weeks for p in phases)
    return {
        "weeks": total,
        "phases": [{"name": p.name, "weeks": p.weeks} for p in phases],
    }


def customer_roi(deployment_cost_total: float, customer_arr: float, gross_margin: float = 0.75, expected_lifespan_years: float = 3.0) -> dict:
    """
    ROI: customer gross profit over expected lifespan vs. deployment cost.
    """
    annual_gross_profit = customer_arr * gross_margin
    total_gross_profit = annual_gross_profit * expected_lifespan_years
    roi = total_gross_profit / deployment_cost_total if deployment_cost_total else 0
    return {
        "customer_arr": customer_arr,
        "gross_margin": gross_margin,
        "expected_lifespan_years": expected_lifespan_years,
        "annual_gross_profit": annual_gross_profit,
        "total_gross_profit": total_gross_profit,
        "deployment_cost": deployment_cost_total,
        "roi": roi,
        "payback_months": (deployment_cost_total / annual_gross_profit * 12) if annual_gross_profit else 0,
    }


def retention_with_vs_without_fde() -> dict:
    """
    Customer retention rate (annual) with and without FDE involvement.
    """
    return {
        "with_fde":    0.92,  # 92% annual retention
        "without_fde": 0.78,  # 78% annual retention
        "delta":       0.14,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="FDE deployment cost, time-to-deployment, customer ROI modeling.")
    parser.add_argument("--fixture", action="store_true", help="Run the example fixture.")
    args = parser.parse_args()

    if args.fixture:
        # Example: 1 FDE deploying for 1 customer at $200K ARR
        print("=== Deployment Cost (1 FDE, 1 customer, $6K/wk loaded) ===\n")
        cost = deployment_cost()
        for phase in cost["phases"]:
            print(f"  {phase['name']:<12} {phase['weeks']:>2} weeks  "
                  f"FDE: ${phase['fde_cost']:>7,.0f}  "
                  f"Other: ${phase['other_cost']:>7,.0f}  "
                  f"Total: ${phase['total']:>8,.0f}")
        print(f"\n  Total: {cost['total_weeks']} weeks, ${cost['total']:,.0f}")

        print("\n=== Time-to-Deployment (Discovery -> Production) ===\n")
        ttd = time_to_deployment()
        for phase in ttd["phases"]:
            print(f"  {phase['name']:<12} {phase['weeks']:>2} weeks")
        print(f"\n  Total: {ttd['weeks']} weeks (~{ttd['weeks']/4.33:.1f} months)")

        print("\n=== Customer ROI ($200K ARR, 75% gross margin, 3-year lifespan) ===\n")
        roi = customer_roi(cost["total_cost"], customer_arr=200_000)
        print(f"  Customer ARR:           ${roi['customer_arr']:>10,.0f}")
        print(f"  Annual gross profit:     ${roi['annual_gross_profit']:>10,.0f}")
        print(f"  Total gross profit:      ${roi['total_gross_profit']:>10,.0f}")
        print(f"  Deployment cost:         ${roi['deployment_cost']:>10,.0f}")
        print(f"  ROI:                     {roi['roi']:>10.1f}x")
        print(f"  Payback period:          {roi['payback_months']:>10.1f} months")

        print("\n=== Customer Retention (with vs. without FDE) ===\n")
        ret = retention_with_vs_without_fde()
        print(f"  With FDE:     {ret['with_fde'] * 100:.0f}% annual retention")
        print(f"  Without FDE:  {ret['without_fde'] * 100:.0f}% annual retention")
        print(f"  Delta:        {ret['delta'] * 100:.0f} pp")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
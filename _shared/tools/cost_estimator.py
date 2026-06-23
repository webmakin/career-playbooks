#!/usr/bin/env python3
"""
cost_estimator.py — Stdlib-only LLM/AI cost estimator.

Estimates per-request and annual cost of an AI feature.

Usage:
    python3 cost_estimator.py --input 1200 --output 350 --model gpt-4o --rpd 28000 --growth 0.25
    python3 cost_estimator.py --list-models
    python3 cost_estimator.py --fixture

Exit codes:
    0  estimate computed
    1  args invalid

All prices in USD per 1M tokens. Verify before sending to a CFO.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"

# Pricing per 1M tokens (USD). (input, output).
# Last reviewed: 2026-06-23. Update quarterly.
PRICING: dict[str, tuple[float, float]] = {
    "gpt-4o":          (2.50, 10.00),
    "gpt-4o-mini":     (0.15, 0.60),
    "gpt-4.1":         (3.00, 12.00),
    "gpt-4.1-mini":    (0.40, 1.60),
    "gpt-4.1-nano":    (0.10, 0.40),
    "o1":              (15.00, 60.00),
    "o1-mini":         (3.00, 12.00),
    "o3":              (10.00, 40.00),
    "o3-mini":         (1.10, 4.40),
    "claude-opus-4":   (15.00, 75.00),
    "claude-sonnet-4": (3.00, 15.00),
    "claude-haiku-4":  (0.80, 4.00),
    "claude-3.5-sonnet": (3.00, 15.00),
    "claude-3-haiku":  (0.25, 1.25),
    "gemini-2.5-pro":  (1.25, 10.00),
    "gemini-2.5-flash": (0.30, 2.50),
    "gemini-2.0-flash": (0.10, 0.40),
    "llama-3.1-405b-self": (3.50, 3.50),
    "llama-3.1-70b-self":  (0.88, 0.88),
    "llama-3.1-8b-self":   (0.18, 0.18),
    "deepseek-v3":     (0.27, 1.10),
    "deepseek-r1":     (0.55, 2.19),
    "mistral-large-2": (2.00, 6.00),
    "mistral-small":   (0.20, 0.60),
    "qwen-3-235b":     (0.20, 0.60),
}


def cost_per_request(input_tok: int, output_tok: int, model: str) -> float:
    if model not in PRICING:
        raise KeyError(f"Unknown model: {model}. Try --list-models.")
    in_price, out_price = PRICING[model]
    return (input_tok / 1_000_000) * in_price + (output_tok / 1_000_000) * out_price


def project(
    input_tok: int,
    output_tok: int,
    model: str,
    rpd: int,
    growth: float,
    growth_period: str = "quarter",
) -> dict[str, float]:
    per_req = cost_per_request(input_tok, output_tok, model)
    per_day = per_req * rpd
    per_month = per_day * 30
    per_year_flat = per_day * 365

    periods_per_year = 4 if growth_period == "quarter" else 1
    if abs(growth) < 1e-9:
        per_year_growth = per_day * 365
    else:
        factor = (1 + growth) ** periods_per_year
        geom_sum = (factor - 1) / growth
        per_year_growth = per_day * geom_sum

    return {
        "per_request": per_req,
        "per_day": per_day,
        "per_month": per_month,
        "per_year_flat": per_year_flat,
        "per_year_growth": per_year_growth,
    }


def fmt_money(x: float) -> str:
    return f"${x:,.2f}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate LLM feature cost.")
    parser.add_argument("--input", type=int, help="Input tokens per request.")
    parser.add_argument("--output", type=int, help="Output tokens per request.")
    parser.add_argument("--model", type=str, help="Model name (see --list-models).")
    parser.add_argument("--rpd", type=int, default=1000, help="Requests per day (default: 1000).")
    parser.add_argument("--growth", type=float, default=0.0, help="Growth rate per period (default: 0).")
    parser.add_argument(
        "--growth-period", choices=["quarter", "year"], default="quarter",
        help="Period over which --growth applies (default: quarter).",
    )
    parser.add_argument("--list-models", action="store_true", help="List known models and exit.")
    parser.add_argument("--fixture", action="store_true", help="Run on bundled fixture.")
    args = parser.parse_args()

    if args.list_models:
        print("Known models (input $/1M, output $/1M):")
        for name in sorted(PRICING):
            in_p, out_p = PRICING[name]
            print(f"  {name:<22} {in_p:>7.2f}  {out_p:>7.2f}")
        return 0

    if args.fixture:
        for (m, inp, outp, rpd, g, period) in [
            ("gpt-4o", 1200, 350, 28000, 0.25, "quarter"),
            ("deepseek-v3", 1200, 350, 28000, 0.25, "quarter"),
        ]:
            print(f"=== Scenario: {m}, {inp} in / {outp} out, {rpd} rpd, growth={g}/q ===")
            res = project(inp, outp, m, rpd, g, period)
            print(f"  Per request:       {fmt_money(res['per_request'])}")
            print(f"  Per day:           {fmt_money(res['per_day'])}")
            print(f"  Per month:         {fmt_money(res['per_month'])}")
            print(f"  Per year (flat):   {fmt_money(res['per_year_flat'])}")
            print(f"  Per year (growth): {fmt_money(res['per_year_growth'])}")
            print()
        return 0

    if not (args.input and args.output and args.model):
        print(
            "cost_estimator: --input, --output, --model are required "
            "(or use --list-models / --fixture)",
            file=sys.stderr,
        )
        return 1

    try:
        res = project(args.input, args.output, args.model, args.rpd, args.growth, args.growth_period)
    except KeyError as e:
        print(f"cost_estimator: {e}", file=sys.stderr)
        return 1

    print(f"=== {args.model}: {args.input} in / {args.output} out, {args.rpd} rpd, growth={args.growth}/{args.growth_period} ===")
    print(f"  Per request:       {fmt_money(res['per_request'])}")
    print(f"  Per day:           {fmt_money(res['per_day'])}")
    print(f"  Per month:         {fmt_money(res['per_month'])}")
    print(f"  Per year (flat):   {fmt_money(res['per_year_flat'])}")
    print(f"  Per year (growth): {fmt_money(res['per_year_growth'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
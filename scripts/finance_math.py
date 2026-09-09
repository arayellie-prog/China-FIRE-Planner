#!/usr/bin/env python3
"""Calculate a minimal financial baseline from JSON using only the stdlib."""

from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation

STATES = {"known", "estimated", "unknown"}
CONFIDENCE = {"high": 2, "medium": 1, "low": 0}


def money(value: object, path: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{path} must be a non-negative number")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError(f"{path} must be a non-negative number") from None
    if not result.is_finite() or result < 0:
        raise ValueError(f"{path} must be a non-negative number")
    return result


def normalize(item: dict, path: str) -> tuple[Decimal | None, str, str | None]:
    status = item.get("status")
    if status not in STATES:
        raise ValueError(f"{path}.status must be known, estimated, or unknown")
    if status == "unknown":
        if item.get("value") is not None:
            raise ValueError(f"{path}.value must be null when status is unknown")
        return None, "unknown", None
    if item.get("value") is None:
        raise ValueError(f"{path}.value is required when status is {status}")
    confidence = item.get("confidence", "medium")
    if confidence not in CONFIDENCE:
        raise ValueError(f"{path}.confidence must be high, medium, or low")
    return money(item["value"], f"{path}.value"), status, confidence


def derived(value: Decimal | None, statuses: list[str], confidences: list[str | None]) -> dict:
    if value is None or "unknown" in statuses:
        return {"value": None, "status": "unknown", "source": "calculated", "confidence": None}
    status = "known" if all(state == "known" for state in statuses) else "estimated"
    valid = [level for level in confidences if level is not None]
    confidence = min(valid, key=CONFIDENCE.get) if valid else "medium"
    return {"value": float(value), "status": status, "source": "calculated", "confidence": confidence}


def total_collection(collection: dict, path: str) -> dict:
    collection_status = collection.get("status")
    if collection_status not in STATES:
        raise ValueError(f"{path}.status must be known, estimated, or unknown")
    if collection_status == "unknown":
        return derived(None, ["unknown"], [])
    values, statuses, confidences = [], [collection_status], []
    for index, row in enumerate(collection.get("items", [])):
        value, status, confidence = normalize(row["amount"], f"{path}.items[{index}].amount")
        if value is None:
            return derived(None, ["unknown"], [])
        values.append(value)
        statuses.append(status)
        confidences.append(confidence)
    return derived(sum(values, Decimal("0")), statuses, confidences)


def calculate(data: dict) -> dict:
    assets = total_collection(data["assets"], "assets")
    liabilities = total_collection(data["liabilities"], "liabilities")
    income_value, income_status, income_conf = normalize(data["monthly_income"], "monthly_income")
    spending_value, spending_status, spending_conf = normalize(data["monthly_spending"], "monthly_spending")

    if assets["value"] is None or liabilities["value"] is None:
        net_worth = derived(None, ["unknown"], [])
    else:
        net_worth = derived(
            Decimal(str(assets["value"])) - Decimal(str(liabilities["value"])),
            [assets["status"], liabilities["status"]],
            [assets["confidence"], liabilities["confidence"]],
        )

    if income_value is None or spending_value is None:
        surplus = derived(None, ["unknown"], [])
        savings_rate = derived(None, ["unknown"], [])
    else:
        statuses = [income_status, spending_status]
        confidences = [income_conf, spending_conf]
        surplus = derived(income_value - spending_value, statuses, confidences)
        rate = None if income_value == 0 else (income_value - spending_value) / income_value
        savings_rate = derived(rate, statuses, confidences) if rate is not None else derived(None, ["unknown"], [])

    return {
        "total_assets": assets,
        "total_liabilities": liabilities,
        "net_worth": net_worth,
        "monthly_surplus": surplus,
        "savings_rate": savings_rate,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="JSON file; omit to read stdin")
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8") if args.input else sys.stdin as stream:
            result = calculate(json.load(stream))
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

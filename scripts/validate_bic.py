#!/usr/bin/env python3
"""Deterministic BIC/SWIFT syntax checker. Not a live directory lookup."""
import argparse
import json
import re

BIC_RE = re.compile(r"^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?$")

def validate_bic(value: str) -> dict:
    normalized = re.sub(r"\s+", "", value or "").upper()
    result = {
        "input": value, "normalized": normalized, "length": len(normalized),
        "syntax_valid": bool(BIC_RE.fullmatch(normalized)), "bic": normalized or None,
        "business_party_code": None, "country_code": None, "location_code": None,
        "branch_code": None,
        "note": "Syntax-only check; this does not confirm current operational status."
    }
    if result["syntax_valid"]:
        result["business_party_code"] = normalized[:4]
        result["country_code"] = normalized[4:6]
        result["location_code"] = normalized[6:8]
        result["branch_code"] = normalized[8:11] if len(normalized) == 11 else None
    return result

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("bic")
    args = p.parse_args()
    print(json.dumps(validate_bic(args.bic), ensure_ascii=False, indent=2))

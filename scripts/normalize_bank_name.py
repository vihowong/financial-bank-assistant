#!/usr/bin/env python3
"""Small deterministic bank-name normalizer. Alias mapping is intentionally conservative."""
import argparse
import json
import re

ALIASES = {
    "bofa": "Bank of America",
    "boa": "Bank of America",
    "bank of america na": "Bank of America, N.A.",
    "bank of america, na": "Bank of America, N.A.",
    "hsbc hong kong": "HSBC Hong Kong",
    "hsbc hk": "HSBC Hong Kong",
    "jpmorgan chase": "JPMorgan Chase Bank, N.A.",
    "jp morgan chase": "JPMorgan Chase Bank, N.A.",
}

def normalize(name: str) -> dict:
    raw = (name or "").strip()
    key = re.sub(r"[\s,]+", " ", raw.lower())
    canonical = ALIASES.get(key, raw)
    return {"input": raw, "normalized_key": key, "canonical_name": canonical, "alias_match": canonical != raw}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("name")
    args = p.parse_args()
    print(json.dumps(normalize(args.name), ensure_ascii=False, indent=2))

#!/usr/bin/env python3
"""Lightweight extraction from pasted transfer instructions. It does not validate live bank data."""
import argparse
import json
import re

PATTERNS = {
    "bic_swift": re.compile(r"\b[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?\b"),
    "iban": re.compile(r"\b[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}\b"),
    "routing_number": re.compile(r"(?i)\b(?:routing(?: number)?|aba)\s*[:#-]?\s*([0-9]{9})\b"),
    "account_number": re.compile(r"(?i)\b(?:account(?: number)?|acct)\s*[:#-]?\s*([A-Z0-9\-]{5,34})\b"),
    "bank_name": re.compile(r"(?i)\b(?:bank(?: name)?|beneficiary bank)\s*[:#-]\s*(.+)")
}

def parse(text: str) -> dict:
    out = {"bic_swift": [], "iban": [], "routing_number": [], "account_number": [], "bank_name": []}
    for kind, pattern in PATTERNS.items():
        for m in pattern.finditer(text or ""):
            value = (m.group(1) if m.lastindex else m.group(0)).strip()
            out[kind].append(value)
    for k in out:
        out[k] = list(dict.fromkeys(out[k]))
    return out

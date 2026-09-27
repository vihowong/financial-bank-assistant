#!/usr/bin/env python3
"""Mask likely account/card-like digit strings while preserving short codes and context."""
import argparse
import re

LONG_DIGITS = re.compile(r"\b\d{8,19}\b")

def mask_text(text: str) -> str:
    def repl(m):
        s = m.group(0)
        return "*" * max(0, len(s) - 4) + s[-4:]
    return LONG_DIGITS.sub(repl, text or "")

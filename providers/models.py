from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class SourceEvidence:
    source_tier: int
    source_type: str
    source_name: str
    source_url: str | None = None
    retrieved_at: str | None = None
    evidence: str | None = None
    freshness: str = "unknown"
    license_note: str | None = None

@dataclass
class ProviderResult:
    ok: bool
    data: dict[str, Any] = field(default_factory=dict)
    sources: list[SourceEvidence] = field(default_factory=list)
    error: str | None = None

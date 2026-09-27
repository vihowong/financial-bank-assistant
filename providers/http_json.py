from __future__ import annotations
import json, os, urllib.error, urllib.parse, urllib.request
from typing import Any
from .models import ProviderResult, SourceEvidence

class NormalizedHTTPProvider:
    """Provider-neutral adapter for a normalized bank-data REST API."""
    def __init__(self, base_url=None, api_key=None, timeout=None):
        self.base_url = (base_url or os.getenv("FBA_LIVE_API_URL", "")).rstrip("/")
        self.api_key = api_key or os.getenv("FBA_LIVE_API_KEY")
        self.timeout = timeout or float(os.getenv("FBA_LIVE_TIMEOUT_SECONDS", "10"))

    @property
    def configured(self): return bool(self.base_url)

    def _get(self, path, params=None):
        if not self.base_url:
            return ProviderResult(ok=False, error="FBA_LIVE_API_URL is not configured")
        query = urllib.parse.urlencode({k:v for k,v in (params or {}).items() if v not in (None,"")})
        url = f"{self.base_url}/{path.lstrip('/')}" + (f"?{query}" if query else "")
        headers = {"Accept":"application/json"}
        if self.api_key: headers["Authorization"] = f"Bearer {self.api_key}"
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                s = data.get("source", {})
                source = SourceEvidence(int(s.get("source_tier",2)), str(s.get("source_type","licensed_api")),
                    str(s.get("source_name","Configured bank-data API")), s.get("source_url",url),
                    s.get("retrieved_at"), s.get("evidence"), str(s.get("freshness","unknown")), s.get("license_note"))
                return ProviderResult(ok=True, data=data, sources=[source])
        except (urllib.error.URLError, TimeoutError) as exc:
            return ProviderResult(ok=False, error=f"Live data request failed: {exc}")
        except (ValueError, json.JSONDecodeError) as exc:
            return ProviderResult(ok=False, error=f"Live data returned invalid JSON: {exc}")

    def search_bank(self, *, query, country=None, city=None): return self._get("search/banks", {"query":query,"country":country,"city":city})
    def lookup_bic(self, bic): return self._get(f"bic/{urllib.parse.quote(bic,safe='')}")
    def validate_bic(self, bic): return self._get(f"validate/bic/{urllib.parse.quote(bic,safe='')}")
    def lookup_identifier(self, country, identifier_type, value):
        return self._get(f"identifiers/{urllib.parse.quote(country,safe='')}/{urllib.parse.quote(identifier_type,safe='')}/{urllib.parse.quote(value,safe='')}")
    def lookup_iban_rules(self, country): return self._get(f"iban/{urllib.parse.quote(country,safe='')}")
    def get_transfer_requirements(self, **kwargs): return self._get("transfer/requirements", kwargs)

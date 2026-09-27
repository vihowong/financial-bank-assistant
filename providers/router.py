from __future__ import annotations
from typing import Any
from .http_json import NormalizedHTTPProvider
from .models import ProviderResult

class ProviderRouter:
    def __init__(self, provider=None): self.provider = provider or NormalizedHTTPProvider()
    def _unavailable(self): return ProviderResult(ok=False, error="No live bank-data provider is configured")
    def search_bank(self, **kwargs): return self.provider.search_bank(**kwargs) if self.provider.configured else self._unavailable()
    def lookup_bic(self, bic): return self.provider.lookup_bic(bic) if self.provider.configured else self._unavailable()
    def validate_bic(self, bic): return self.provider.validate_bic(bic) if self.provider.configured else self._unavailable()
    def lookup_identifier(self, **kwargs): return self.provider.lookup_identifier(**kwargs) if self.provider.configured else self._unavailable()
    def lookup_iban_rules(self, country): return self.provider.lookup_iban_rules(country) if self.provider.configured else self._unavailable()
    def get_transfer_requirements(self, **kwargs): return self.provider.get_transfer_requirements(**kwargs) if self.provider.configured else self._unavailable()

"""Optional MCP server for Financial Bank Assistant."""
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
from providers.router import ProviderRouter
from scripts.validate_bic import validate_bic as local_validate_bic
from scripts.parse_transfer_data import parse as parse_transfer_data
from scripts.mask_sensitive_data import mask_text
try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise RuntimeError("The optional MCP server requires the 'mcp' Python package.") from exc

mcp = FastMCP("financial-bank-assistant")
router = ProviderRouter()

def _result(r):
    return {"ok":r.ok,"data":r.data,"sources":[s.__dict__ for s in r.sources],"error":r.error}

@mcp.tool()
def search_bank(query: str, country: str | None = None, city: str | None = None) -> dict:
    return _result(router.search_bank(query=query,country=country,city=city))

@mcp.tool()
def lookup_bic(bic: str) -> dict:
    return _result(router.lookup_bic(bic))

@mcp.tool()
def validate_bic(bic: str) -> dict:
    return {"local":local_validate_bic(bic),"live":_result(router.validate_bic(bic))}

@mcp.tool()
def lookup_identifier(country: str, identifier_type: str, value: str) -> dict:
    return _result(router.lookup_identifier(country=country,identifier_type=identifier_type,value=value))

@mcp.tool()
def lookup_iban_rules(country: str) -> dict:
    return _result(router.lookup_iban_rules(country))

@mcp.tool()
def get_transfer_requirements(source_country: str, destination_country: str, source_bank: str | None=None, destination_bank: str | None=None, currency: str | None=None, transfer_type: str="international_wire") -> dict:
    return _result(router.get_transfer_requirements(source_country=source_country,destination_country=destination_country,source_bank=source_bank,destination_bank=destination_bank,currency=currency,transfer_type=transfer_type))

@mcp.tool()
def check_transfer_data(data: dict, source_country: str | None=None, destination_country: str | None=None, currency: str | None=None) -> dict:
    raw="\n".join(f"{k}: {v}" for k,v in data.items())
    requirements=router.get_transfer_requirements(source_country=source_country,destination_country=destination_country,currency=currency,transfer_type="international_wire")
    return {"input_fields":list(data.keys()),"parsed":parse_transfer_data(raw),"masked_preview":mask_text(raw),"live_requirements":_result(requirements),"note":"Preflight assistance only; not a guarantee of bank acceptance."}

if __name__ == "__main__":
    mcp.run()

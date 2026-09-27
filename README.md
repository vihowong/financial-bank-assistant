# Financial Bank Assistant v0.2

Financial Bank Assistant is an Agent Skill for non-expert users who need to find banks, understand banking identifiers, prepare international transfers, and check beneficiary/bank data before submitting a payment.

## v0.2 focus: live data layer

v0.2 introduces a provider-neutral live-data architecture:

- normalized REST provider adapter (`providers/http_json.py`)
- provider router with explicit unavailable state (`providers/router.py`)
- MCP tool server (`mcp_server/server.py`)
- normalized MCP schemas (`references/mcp-contract.md`)
- source/evidence model
- current web verification playbook
- deployment environment template

The skill does **not** ship a proprietary BIC/bank directory. Production deployment should connect a licensed/authorized banking-data provider or bank-owned data source.

## Install/test locally

```bash
python -m unittest discover -s tests -v
```

Optional MCP deployment dependency:

```bash
pip install mcp
```

Configure the live normalized bank-data service:

```bash
export FBA_LIVE_API_URL="https://your-provider.example.com"
export FBA_LIVE_API_KEY="..."
```

See `references/mcp-contract.md` for the endpoint contract.

## Important deployment rule

Do not add `agents/openai.yaml` until the real remote MCP endpoint is deployed. The manifest must contain the real endpoint, not a placeholder URL.

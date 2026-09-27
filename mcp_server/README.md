# MCP server

This folder contains the optional MCP server for Financial Bank Assistant.

The folder name is intentionally `mcp_server` rather than `mcp` so it does not shadow the official `mcp` Python package.

## Deployment

Install the MCP SDK in the deployment environment:

```bash
pip install mcp
```

Configure the live normalized bank-data service:

```bash
export FBA_LIVE_API_URL="https://your-normalized-bank-data-api.example.com"
export FBA_LIVE_API_KEY="..."
```

See `../references/mcp-contract.md` for the endpoint contract.

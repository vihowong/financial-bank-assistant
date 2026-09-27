# MCP Tool Contract

The skill expects a normalized MCP server backed by a commercial/authorized bank-data backend, internal bank directory, or permitted verification service.

## Tools
- `search_bank`
- `lookup_bic`
- `validate_bic`
- `lookup_identifier`
- `lookup_iban_rules`
- `get_transfer_requirements`
- `check_transfer_data`

## Example input
```json
{"query":"HSBC","country":"HK","city":"Hong Kong"}
```

## Transfer requirements input
```json
{"source_country":"US","destination_country":"HK","source_bank":"Chase","destination_bank":"HSBC Hong Kong","currency":"USD","transfer_type":"international_wire"}
```

## Output requirements
Material responses should expose fields present/missing, conflicts, identifier checks, source evidence, confidence/uncertainty, and checked time. Never imply that a syntax check alone proves a code is active.

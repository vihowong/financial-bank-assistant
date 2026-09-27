# Live Data Layer

## Goal
The live-data layer turns Financial Bank Assistant from a static knowledge skill into a verification workflow. It should return structured evidence, not only strings.

## Normalized source record
Every material lookup should retain source tier, type, name, URL, retrieval time, evidence, freshness, and license note.

## Source tiers
1. Official bank/SWIFT/ISO/official registry.
2. Licensed or authorized provider.
3. Reputable public secondary source.
4. General web search for discovery/cross-check only.

## Current official references
- SWIFT BIC overview: https://www.swift.com/standards/data-standards/bic-business-identifier-code
- SWIFT standards resources: https://www.swift.com/standards/standards-resources
- SWIFTRef Identifiers Directory: https://www.swift.com/products/swiftref-identifiers-directory
- SWIFTRef BIC Directory: https://www.swift.com/products/swiftref-bic-directory

Do not hard-code proprietary directory data into the skill without permission.

## BIC validation model
1. Syntax validation is deterministic and may be local.
2. Entity mapping requires a credible data source.
3. Current operational status requires current authoritative evidence.

## Web fallback
When no MCP provider is configured, find the bank's current official wire instructions and a current authoritative BIC reference, compare values, record dates, and report conflicts.

## Provider strategy
The bundled provider is provider-neutral and uses:
- FBA_LIVE_API_URL
- FBA_LIVE_API_KEY
- FBA_LIVE_TIMEOUT_SECONDS

Expected endpoints:
- GET /search/banks
- GET /bic/{bic}
- GET /validate/bic/{bic}
- GET /identifiers/{country}/{identifier_type}/{value}
- GET /iban/{country}
- GET /transfer/requirements

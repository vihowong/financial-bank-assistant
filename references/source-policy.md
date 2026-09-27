# Source Policy

## Priority
1. Destination/sending bank official current wire instructions.
2. SWIFT / ISO / relevant government or official banking registry.
3. Licensed or authorized financial-data provider.
4. Reputable public secondary source.
5. General search results.

## Materiality
Material facts include:
- BIC/SWIFT value.
- Current bank status.
- Branch identity.
- Required transfer fields.
- Fees.
- Current transfer timing.
- Current routing details.

For material facts, show source context whenever practical.

## Conflict handling
If sources disagree:
- Prefer the newer authoritative source.
- Check whether the disagreement is about 8-vs-11 character BIC representation, old vs new legal entity, branch vs head office, or stale data.
- Do not silently choose a value if the conflict could change a real transfer.
- Tell the user to use the receiving bank's current wire instructions when needed.

## Reference sources
- ISO 9362: https://www.iso.org/standard/84108.html
- ISO 13616: https://www.iso.org/standard/81090.html
- SWIFT BIC: https://www.swift.com/standards/data-standards/bic-business-identifier-code
- OpenAI Skills: https://developers.openai.com/api/docs/guides/tools-skills

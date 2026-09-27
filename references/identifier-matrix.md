# Banking Identifier Matrix

This reference is a routing aid, not a substitute for the receiving bank's current instructions.

| Market | Common identifiers | Notes |
|---|---|---|
| United States | ABA/Routing Number, SWIFT/BIC | Routing is common for domestic rails; international wires may request BIC and/or routing details depending on bank and corridor. |
| United Kingdom | Sort Code, Account Number, IBAN, SWIFT/BIC | Requirement depends on domestic vs international payment. |
| European IBAN countries | IBAN, BIC/SWIFT | IBAN structure varies by country under ISO 13616 registration. |
| Hong Kong | Bank Code, Branch Code, Account Number, SWIFT/BIC | Bank-specific instructions determine exact fields. |
| Singapore | Bank Code, Branch Code, Account Number, SWIFT/BIC | Bank/channel-specific. |
| India | IFSC, Account Number, SWIFT/BIC | IFSC is primarily a domestic Indian identifier; international payments may require BIC/SWIFT. |
| Australia | BSB, Account Number, SWIFT/BIC | BSB is a domestic routing identifier. |
| Canada | Institution Number, Transit Number, Account Number, SWIFT/BIC | Exact international wire fields depend on bank/channel. |
| Japan | Bank Code, Branch Code, Account Number, SWIFT/BIC | Exact requirements are bank-specific. |
| China | Bank/branch identifiers and SWIFT/BIC | Exact fields vary with bank, currency, and receiving instructions. |

Rules:
- Never infer that a local identifier replaces SWIFT/BIC for an international transfer unless the bank instructions say so.
- Never infer that SWIFT/BIC replaces a local identifier where the bank explicitly asks for both.
- Always prefer destination-bank instructions for the final field list.

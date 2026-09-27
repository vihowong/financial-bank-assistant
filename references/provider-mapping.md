# Provider Mapping

## SWIFT

For high-assurance BIC and cross-referenced bank identifiers, the preferred production data family is SWIFT's SwiftRef portfolio. SWIFT describes its Identifiers Directory as global reference data collected from central banks, code issuers, clearing and settlement mechanisms, banking associations, regional financial communities, and financial institutions.

Commercial integration requires the applicable SWIFT subscription/license. Do not ship a copied proprietary BIC/identifier database in this skill without permission.

## Wise

Wise provides a public BIC/Swift code checker for format checking and bank identification. Wise Platform also provides APIs for partner integrations, but those APIs are primarily for Wise Platform transfer/account functionality rather than a universal BIC-directory replacement. Use Wise as a secondary public reference unless the specific API contract gives the required bank-directory data.

## Bank official pages

For a concrete payment, the receiving bank's current incoming-wire instructions are often the most relevant evidence for the exact fields the bank wants customers to use.

## IBAN

Use the latest official SWIFT IBAN Registry for country-level IBAN structure. Cache only when licensing and update rights permit it.

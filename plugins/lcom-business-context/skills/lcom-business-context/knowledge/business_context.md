# Business Context

## Systems and Sources of Authority

- Salesforce is the current master system for commercial information.
- LCom Platform is the primary source for operational organization hierarchy,
  licensing, users, and product usage.
- HubSpot is the originating master system for some ECommerce transactions.
- NetSuite contains financial/order information and was the primary commercial
  system before the migration to Salesforce.
- HubSpot and NetSuite information is loaded into Salesforce but may be overriten in Salesforce 
- Salesforce information is loaded in HubSpot and NetSuite. It might be used partially in the processes, how exactly is unknown.
- Enterprise data warehouse combine commercial information (Salesforce) and operational organization hierarchy,
  licensing, users, and product usage (LCom Platform) in a conformed system.

## Business Governance

- Many business rules are operational practices rather than formally governed policies.
- Business rules do not consistently have a designated business owner.
- Some classifications and processes are manually maintained.
- When ownership or authoritative interpretation is not documented, it should
  be treated as unknown rather than inferred.

## Data and Process Reality

- Business data is not assumed to be perfectly clean or internally consistent.
- Manual processes, backdated transactions, missing relationships, and historical
  system migrations can affect reporting.
- Differences between systems do not automatically mean one system is incorrect;
  systems may represent different business perspectives.

## Interpretation Principle

- Use entity-specific ontology rules when they exist.
- Entity-specific rules override general context.
- Do not invent a business rule when the available knowledge identifies an
  ambiguity or missing ownership.
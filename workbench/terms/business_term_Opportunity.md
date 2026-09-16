# Contract / Opportunity

A **Contract / Opportunity** represents a commercial transaction or potential commercial transaction with an Account. **Opportunity** is the broader lifecycle concept and can represent business that is still in progress, won, lost, renewed, upsold, or adjusted. A **Contract** is a qualified Opportunity: an Opportunity is considered an **Active Contract** when it is Won and has an Invoiced Date. Active Contracts contribute to company bookings and ARR.

Contracts are commonly annual, but they may also be shorter-term with annualized revenue or multi-year. Renewal relationships represent commercial continuity but are not always complete or one-to-one. 

If a renewal is still pending, the existing contract may remain active past its End Date to allow early access to LCom Platform.

Backdated opportunities are common when Invoiced Date is after Start Date.

- An Opportunity may contain one or more **Opportunity Line Item / Deals**, so it should not always be interpreted as a single commercial type.
- An Opportunity that is neither Won nor Lost is treated as an **Active Renewal**.
- A child Opportunity may renew more than one parent Opportunity.

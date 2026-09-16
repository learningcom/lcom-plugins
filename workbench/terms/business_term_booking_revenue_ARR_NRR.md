# Booking

**Booking** represents the value of customer contracts that have been successfully sold and recorded through **Closed Won Opportunities with an Invoiced Date**. Depending on the report, Bookings are assigned to a reporting period using the Invoiced Date or **Close Date. These dates fall in the same month for most Opportunities.

Booking includes both the **recurring (ARR)** and **non-recurring (NRR)** portions of the contract, including applicable multi-year amounts.

# Revenue

**Revenue** is the value of products and services recognized as earned during a reporting period. For subscription products, revenue is generally recognized over the period in which the customer receives the service.

# Annual Recurring Revenue (ARR)

**Annual Recurring Revenue (ARR)** represents the recurring contractual value of active subscription business. ARR includes only the recurring portion of a Deal and is reported for each month in which that value is active.

**ARR** is different from **Booking** in a few key ways. **ARR includes only the recurring contractual value of a Deal** and is **reported for each month in which that value is active**.

ARR is typically viewed across the company’s fiscal year, which generally aligns with the Start and End periods of most contracts.

### Business Questions

- How much ARR do we have in this month by Account, Customer, State, Product, or for the company as a whole?
- Why did our ARR change?

# Non-Recurring Revenue (NRR)

**Non-Recurring Revenue (NRR)** is revenue that we expect to receive from our customers for providing them with products or services on a one-time, non-recurring basis. An example of NRR is a full day of professional development training for a district.

NRR also covers products that are typically sold as subscriptions for periods longer than 12 months. The first year of such subscriptions is classified as ARR, and the remaining contract period is classified as NRR.

# Opportunity / Deal ARR and NRR

**Opportunity / Deal ARR and NRR** describe how the **booked** value of an Opportunity or Deal is **classified**.


- **Opportunity / Deal ARR** is the **recurring** portion of the **booked** Opportunity or Deal and represents the recurring value sold.
- **Opportunity / Deal NRR** is the **non-recurring** portion of the **booked** Opportunity or Deal and represents one-time services or applicable multi-year amounts.


For **paid-up-front multi-year Deals**, the first 12 months are classified as **ARR**, while the remaining contract value is classified as **NRR** using the multi-year categories **Upfront Yr 2&3** and **Upfront Yrs >3**.

These values are attributed to a reporting period based on the applicable Opportunity date, such as the **Invoiced Date** or **Close Date**.

**Business question:** How much is this deal worth?

# In simple terms

- **Booking** = total value sold
- **Opportunity / Deal ARR** = recurring portion of the Deal
- **Opportunity / Deal NRR** = non-recurring or applicable multi-year portion of the Deal
- **Revenue** = value earned during the reporting period
- **ARR** = recurring contractual value active during the reporting period

# Examples

### 12-Month Contract

A district purchases EasyTech for a full school year, from **July 1 through June 30**, for a total contract value of **$13,000**.

The Opportunity contains two line items:

- **$12,000 EasyTech subscription**, classified as ARR
- **$1,000 professional services webinar**, classified as NRR

For this contract:

- **Opportunity / Deal ARR:** $12,000
- **Opportunity / Deal NRR:** $1,000
- **Total Booking:** $13,000, reported in the month determined by the **Invoiced Date or Close Date**, depending on the report
- **Revenue:** $1,000 per month from July through June for the EasyTech subscription, plus $1,000 in the month when the professional service is provided
- **ARR:** $12,000 reported in each month from July through June while the contract is active

### 6-Month Contract

A district purchases EasyTech partway through the school year for **6 months**, from **January 1 through June 30**, for **$6,000**.

The Opportunity contains one line item:

- **$6,000 EasyTech subscription**, classified as ARR

The subscription price is **prorated** because the initial contract covers only 6 months.

For this contract:

- **Opportunity / Deal ARR:** $6,000
- **Opportunity / Deal NRR:** $0
- **Total Booking:** $6,000, reported in the month determined by the **Invoiced Date or Close Date**, depending on the report
- **Revenue:** $1,000 per month from January through June
- **ARR:** $6,000 reported in each month from January through June while the contract is active

If the district then renews for a full 12-month term at **$12,000**:

- **Opportunity / Deal ARR:** $12,000
- **Opportunity / Deal NRR:** $0
- **Renewal Booking:** $12,000
- **Revenue:** $1,000 per month
- **ARR:** $12,000 reported in each month from July through June of the next fiscal year

### 2-Year Contract

A district purchases EasyTech for **2 years**, from **July 1 through June 30 two years later**, for a total contract value of **$24,000**, paid up front.

The Opportunity contains two line items:

- **$12,000 for Year 1**, classified as ARR
- **$12,000 for Year 2**, classified as NRR / multi-year revenue

For this contract:

- **Opportunity / Deal ARR:** $12,000
- **Opportunity / Deal NRR:** $12,000
- **Total Booking:** $24,000, reported in the month determined by the **Invoiced Date or Close Date**, depending on the report
- **Revenue:** $1,000 per month over the 24-month contract period
- **ARR:** $12,000 reported in each month of the first contract year while the ARR portion is active

The second-year amount is included in the total Booking but is classified as **NRR** because it represents the prepaid value of a future contract year rather than first-year ARR.

# ARR Types

The current methodology supports three complementary types of ARR. Each is calculated from the same underlying Salesforce opportunity data but applies different rules around timing, confirmation, and the treatment of recent renewal activity.

| ARR View | Primary Use | Description |
|---|---|---|
| **True ARR** | Actuals-based reference view | Recognizes ARR only when payment is received for won contracts or cancellation is confirmed for lost contracts. ARR decreases when contracts expire without renewal. |
| **Backdated ARR** | Finance and adjusted historical reporting | Ties ARR to the contract Start Date, but only after payment is received or cancellation is confirmed. Historical periods are retroactively adjusted when new information becomes available. |
| **Preliminary ARR** | Financial budget planning and recent/current estimated reporting | Uses standardized grace periods to estimate ARR while renewal and payment information is still emerging. Grace periods are 6 months for State / Biz Dev deals, 90 days for Texas accounts, and 60 days for other district accounts. Recognizes ARR only when payment is received for won contracts or cancellation is confirmed for lost contracts. |



For more details, see **ARR Methodology, Framework and Definitions**.






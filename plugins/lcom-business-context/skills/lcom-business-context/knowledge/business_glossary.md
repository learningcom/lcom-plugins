# Business Glossary

## Contents

- [Fiscal and School Year Calendar](#fiscal-and-school-year-calendar)
- [Account](#account)
- [LCom Customer](#lcom-customer)
- [Contact](#contact)
- [CSM (Customer Success Manager)](#csm-customer-success-manager)
- [Contract / Opportunity](#contract-opportunity)
- [Opportunity Line Item / Deal](#opportunity-line-item-deal)
- [Booking](#booking)
- [Churn](#churn)
- [Product](#product)
- [License Order](#license-order)
- [License Provisioning Method](#license-provisioning-method)
- [User](#user)
- [Enrollment](#enrollment)
- [Usage](#usage)
- [Usage Metrics](#usage-metrics)
- [Training Session](#training-session)
- [Case](#case)

---

## Fiscal and School Year Calendar

Learning.com uses a custom **Fiscal Year calendar** that runs from **July 1 through June 30**. It is aligned with the commonly used **School Year** cycle to make financial and educational activity easier to compare, although individual schools and districts may follow different academic calendars.

A year is identified by the **two calendar years it spans**, using the format **YYYY/YYYY**. For example, **2025/2026** represents July 1, 2025 through June 30, 2026.

- **July = Month 1**
- **August = Month 2**
- …
- **June = Month 12**
- The July–June convention is used for both Fiscal Year and School Year reporting.

[↑ Back to Contents](#contents)

---

# Account

An **Account / Organization** represents a public or commercial educational organization that has, had, or may have a relationship with Learning.com. This can include schools, districts, state education organizations, private schools, and other organizations that purchase products, hold licenses, use Learning.com products, receive services, or exist as prospects.

An Account has both an **operational** and a **commercial** context, and these do not always align. Operationally, schools and districts represent where licenses and product usage occur. Commercially, revenue can be assigned to any level of account hierarchy.

- A typical public-education structure is **School → District**.
- Commercial organizations are grouped under a **Customer**, defined as the **Salesforce Ultimate Parent Account**. They may have additional intermediate levels, but for reporting purposes the hierarchy is represented as **School → District → Customer**.
- An individual low-level account such as a school is not counted as a company customer even if revenue is associated directly with that school; it is reported under its parent account like District or Customer along with other schools in this district.
- Most accounts both pay for and use Learning.com products, but some arrangements—particularly **State Program Deals**—have one account (like a State Department of Education) paying while other accounts (public districts and schools) receive licenses and generate usage.
- Licenses are always provisioned at the District level
- Product Usage mostly collected at the School level with small amount at the District level when a school can not be defined from the data

[↑ Back to Contents](#contents)

---

# LCom Customer

An **LCom Customer** is an organization at the **Customer / Ultimate Parent level** with **non-zero ARR from active contracts**. It represents the organization counted as a customer when answering business questions such as **“How many customers does Learning.com have?”**

Revenue may come from contracts associated with different Accounts within the Customer hierarchy. Individual Accounts—such as schools or Accounts in the District role—are **not counted as separate LCom Customers**, even when they have their own active contracts and non-zero ARR. Their revenue contributes to their Customer / Ultimate Parent.

- When an LCom Customer’s total ARR becomes **$0**, the Customer is considered **churned**.
- Holding licenses or using Learning.com products does **not** make an organization an LCom Customer.
- Districts and schools using products through a **State Program Deal** are license holders/product users, not separate LCom Customers, unless they belong to a different Customer / Ultimate Parent with its own non-zero ARR.
- Because these license holders are not LCom Customers, losing their State Program access or usage is **not customer churn**.

[↑ Back to Contents](#contents)

---

# Contact

A **Contact** is an individual person associated with an **Account**, **Opportunity**, and/or **Marketing Campaign**. A Contact may also have an assigned owner and marketing lifecycle or qualification information, such as **MQL**, **SQL**, **Rejected**, and **Returned**.

Contacts may originate in **Salesforce** or **HubSpot**. When the same Contact exists in both, marketing lifecycle or qualification dates may not be consistent, and an authoritative source or precedence for conflicting dates is not currently defined.

[↑ Back to Contents](#contents)

---

# CSM (Customer Success Manager)

## Definition

A **Customer Success Manager (CSM)** is a person responsible for helping **LCom Customers** get value from the **LCom Platform**.

## Related Ownership Roles

- **Account Owner** — the primary representative responsible for the overall customer account relationship.
- **Opportunity Owner** — the sales representative or business developer responsible for a specific opportunity or deal.

These roles are related to customer management but represent different responsibilities and should not be treated as interchangeable.

[↑ Back to Contents](#contents)

---

# Contract / Opportunity

A **Contract / Opportunity** represents a commercial transaction or potential commercial transaction with an Account. **Opportunity** is the broader lifecycle concept and can represent business that is still in progress, won, lost, renewed, upsold, or adjusted. A **Contract** is a qualified Opportunity: an Opportunity is considered an **Active Contract** when it is Won and has an Invoiced Date. Active Contracts contribute to company bookings and ARR.

Contracts are commonly annual, but they may also be shorter-term with annualized revenue or multi-year. Renewal relationships represent commercial continuity but are not always complete or one-to-one. 

If a renewal is still pending, the existing contract may remain active past its End Date to allow early access to LCom Platform.

Backdated opportunities are common when Invoiced Date is after Start Date.

- An Opportunity may contain one or more **Opportunity Line Item / Deals**, so it should not always be interpreted as a single commercial type.
- An Opportunity that is neither Won nor Lost is treated as an **Active Renewal**.
- A child Opportunity may renew more than one parent Opportunity.

[↑ Back to Contents](#contents)

---

# Opportunity Line Item / Deal

An **Opportunity Line Item**, also called an **individual Deal**, is the individual product and revenue component within an Opportunity / Contract. An Opportunity may contain one or several Deals, allowing the same contract to include different products, revenue types, or portions of a multi-year agreement.

Each Deal identifies what is being sold, its price, quantity, amount, discounts, and **Class**. Class describes both the commercial motion—**New Business, Renewal, or Upsell**—and the revenue type, such as **ARR, Biz Dev, NRR, or multi-year revenue**.

- A single Opportunity can contain Deals with different classifications.
- ARR and Biz Dev are both recurring revenue but represent different types of business.
- NRR represents products or services that are not expected to renew annually.
- **Upsell versus a Renewal price increase**, depend on the full Opportunity and the Account's previous history and cannot be analyzed from one Deal alone.

[↑ Back to Contents](#contents)

---

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

[↑ Back to Contents](#contents)

---

# Churn

**Churn** occurs when an **LCom Customer’s total ARR becomes $0**. The LCom Customer is then considered **churned** and is no longer counted as a current LCom Customer.

Churn is determined at the **Customer / Ultimate Parent level**, not at the individual Account, District or School level.

- A school or District-role Account losing its own ARR does not represent churn if its Customer / Ultimate Parent still has non-zero ARR from other schools or districts.
- The expiration or loss of a license does not by itself represent churn.
- Districts and schools that participate only through a **State Program Deal** are not LCom Customers and therefore cannot churn.
- If a churned LCom Customer later has non-zero ARR again, it becomes a **Returning LCom Customer**.

[↑ Back to Contents](#contents)

---

# Product

**Product** is a common term for an LCom offering, but it does not have one single definition across sales, licensing and learning content. The fundamental concept is the **Learning Item (Lesson)**. Lessons are packaged and organized in overlapping ways for sale, licensing, and delivery to students.

Products are sold through commercial product definitions in Salesforce and licensed in the LCom Platform through **SKUs**. Licensed lessons are delivered through **Sequences** and a **Default Pathway**; teachers and district coordinators can also create **Custom Sequences** from available lessons. Usage is measured at the Lesson level and cannot be reliably attributed to a Salesforce Product or specific licensed SKU, so **Product Categories** are used to group usage for product reporting.

- Salesforce Products and licensing SKUs have a many-to-many relationship rather than a one-to-one mapping.
- Sequences, Custom Sequences, and Default Pathways organize and deliver lessons; they are not independently sold or licensed products.
- SKU, Sequences, Custom Sequences, and Default Pathways have a many-to-many relationship with lessons rather than a one-to-one or one-to-many mapping.
- Product Categories support usage reporting but do not provide a common product structure for revenue and licensing.
- Product Categories are built based on SKU or sequences.  
- Product Categories may overlap based on lessons, so usage totals across categories are not additive.
- Salesforce sub-families do not represent all complexity of recognized Product Categories but most close concept defined in Salesforce to report revenue

[↑ Back to Contents](#contents)

---

# License Order

A **License Order** represents licensing for an LCom District for a defined period and LCom Product. It is created from a **Salesforce Opportunity Line Items** and includes **License Provisioning**, usually expressed as a number of students, along with the schools covered by the order. License Provisioning represents how many students Learning.com is paid to serve and is an estimate of potential student use rather than a limit on how many individual users may access the platform.

**License Provisioning should not be confused with Active Users.** Active Users are users, mostly students, who have actually started using the LCom Platform. Because the provisioned quantity does not limit access, actual users can exceed License Provisioning. Provisioning is maintained for the District-level order and is not allocated to individual schools, so it cannot be used to determine accurate school-level provisioning or utilization.

- License Orders have Start and End dates and may be enforced or unenforced.
- Late-closing contracts can create backdated License Orders and change historical active-license counts.
- License Orders may be manually unenforced to provide early access while a late-payment renewal is unresolved.

[↑ Back to Contents](#contents)

---

# License Provisioning Method

**License Provisioning Method** determines how License Provisioning is calculated for a reporting month.

The standard calculation is **Max Students**: for each District, report the highest number of students from License Orders that are active during the selected month. The licensed SKU is ignored. **Early Access** uses the same calculation but also includes an expired License Order when it is marked **Not Enforce Date Restrictions**.

For Districts marked as **State Initiative**, provisioning can instead be calculated using special EasyTech rules:
- **Florida and Mississippi:** EasyTech K–12
- **Georgia, Michigan, Mississippi, North Carolina, South Carolina, and West Virginia:** EasyTech K–8

The available methods combine these rules as follows:

| Method | State Initiative District | Other Districts | Early Access |
|---|---|---|---|
| **Max Students** | Max Students | Max Students | No |
| **Early Access Max Students** | Max Students | Max Students | Yes |
| **State Initiative then Max Students** | State Initiative calculation | Max Students | No |
| **Early Access State Initiative then Max Students** | State Initiative calculation | Max Students | Yes |
| **State Initiative Students** | State Initiative calculation | 0 | No |
| **Early Access State Initiative Students** | State Initiative calculation | 0 | Yes |

**Max Students** is considered the most accurate measure of License Provisioning because it uses active License Orders and does not apply State Initiative substitutions or Early Access treatment.

### Historical reporting

License Provisioning is currently calculated using the information available **today**. Because License Orders can be added or changed later with dates in the past, a historical month can show a different value when viewed several months later. In other words, the report answers **“what do we now know was active in that month?”**, not necessarily **“what did the number look like at that time?”**

A License Order is counted if it was active on **any day during the month**, rather than only if it was active on the last day of the month. This can produce a higher monthly value because orders that ended earlier in the month are still included. It also makes the metric more complex to calculate, test, and explain.

It is possible to report a historical snapshot that excludes later backdated changes, showing the number that would have been visible at the time. Another simpler option is to count only License Orders active on the **last day of each month** and, for the current month, active **today**. This produces a more stable metric that is easier to compare and validate over time.

**Opportunity Closed Won Students** is a separate comparison measure. It reports the maximum number of students from Closed Won, invoiced Opportunities that are active in the selected month.

[↑ Back to Contents](#contents)

---

# User

A **User** is a student, teacher, or district coordinator who uses an LCom Product. Users are associated with a district, and students and teachers may also be associated with a school.

For internal LCom business reporting, Users are mainly counted to understand product usage rather than to identify individuals. A student’s school or grade may change over time, so reporting can include both current and historical enrollment context. User names and emails are not currently used for this reporting.

[↑ Back to Contents](#contents)

---

# Enrollment

**Enrollment** is the number of students associated with a school or district. Enrollment data may come from LCom Platform rosters maintained by teachers and district coordinators or from NCES enrollment data.

Enrollment should be treated as an **estimate rather than an exact count**. LCom Platform enrollment may include students or schools that are not using the platform and may retain students who have left. NCES data may be outdated, and school enrollment totals may not always match district enrollment totals.

[↑ Back to Contents](#contents)

---

# Usage

**Usage** represents interactions by Users with Learning Items in the LCom Platform, such as launching or completing a lesson. Each Usage event is associated with a User, a Learning Item, a Grade, and an organization—normally a School, or a District when the School is not available.

Learning Items can be organized in several independent ways, including Topic, SKU, Sequence, Unit, Default Path, and Product Category. These groupings do not form a single hierarchy, and a specific Usage event cannot be reliably tied to the particular licensed SKU or Salesforce Product that provided access.

- The same User may launch or complete the same Learning Item more than once.
- Product Categories can overlap because a Learning Item may belong to more than one category, so totals across categories are not additive.
- Unique User counts are also non-additive across organizational levels. Summing School-level unique Users is accepted as an approximation for higher levels, with an observed difference of approximately 2% or less from the exact distinct count.

[↑ Back to Contents](#contents)

---

# Usage Metrics

Usage metrics summarize User activity in the LCom Platform since the start of the school year.

- **Active Users** — unique students, teachers, and district coordinators with at least one Launch.
- **Launches** — unique Launch events.
- **Users with Completions** — unique students, teachers, and district coordinators with at least one Completion.
- **Completions** — Completion events.

**Active Users** and **Users with Completions** are generally non-additive because the same User can appear under more than one School. For example, a student who moves Schools but keeps the same User ID is counted in both Schools but only once at a higher level.

In practice, School-level unique User counts are summed for higher-level totals. The difference from the exact company-wide distinct count is approximately **2% or less**, so this approximation is accepted.

[↑ Back to Contents](#contents)

---

# Training Session

A **Training Session** is a Learning.com professional training activity. It records the training being planned or delivered, including who requested and delivers it, the topics covered, attendance and implementation information, and post-training feedback.

The Account associated with the Training Session is not always the Account that paid for it. For example, a District or Customer may purchase training that is delivered through separate Training Sessions for individual Schools. Training is paid for through an Opportunity, but the Training Session does not have a direct relationship to that Opportunity in the available data.

- A Training Session is requested by a **CSM** and may first be assigned to a training group before being assigned to a specific trainer.
- One Training Session can cover **multiple Topics**.
- Training Session information is entered manually and may be incomplete or inconsistent.
- Survey responses are manually matched to the appropriate Training Session and copied into the record rather than being directly linked to the session.

[↑ Back to Contents](#contents)

---

# Case

A **Case** is a Salesforce record used to track a customer question, issue, or support request from creation through resolution. A Case is associated with an **Account**, a **Contact**, and an **Employee who owns the Case**.

Cases include information about the request, its status and dates, ownership, escalation, and resolution. They can also be classified by attributes such as **Origin, Priority, Case Type, Support Type,** and **Platform Name**;

[↑ Back to Contents](#contents)

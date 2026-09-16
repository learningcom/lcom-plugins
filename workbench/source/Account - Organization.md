# Account / Organization Entity at Learning.com

An **Account/Organization** represents a public educational organization (such as a public school or district) or a commercial educational organization (such as a private school, summer camp, or after-school program) that can participate in one or more relationships with Learning.com: it may purchase Learning.com products, hold licenses, contain users, consume the LCom Platform lessons, open techival support cases, receive trainings or simply exist as a prospective or reference organization.

There is no single source-system representation of this entity within the company. Its identity and hierarchy are distributed primarily between **LCom Platform Organizations** and **Salesforce Accounts**, with additional account creation or synchronization paths involving HubSpot and NetSuite.

## LCom Platform Organizations

LCom Platform represents the **operational/product side** of the organization. Its organization hierarchy has two primary levels:

```text
District
   ├── School
   ├── School
   └── School
```

Licenses are associated with districts. Users—including students, teachers, and district coordinators—can be associated with either a district or a school.

Usage is therefore predominantly school-level but is not necessarily associated with a real school. District users can generate usage under the district organization itself or under a **generic school-level organization**, with names such as `Cloud`, `*cloud`, or similar variants, created to represent school-level usage for district users. Consequently, a school-level LCom Organization should not automatically be interpreted as a physical school.

LCom Organizations may also have a specific deletion lifecycle. Organizations can be effectively **soft-deleted through naming conventions** rather than physically removed. Names can be prefixed or otherwise modified with variations of `z`, `Z*`, `do not use`, etc., with inconsistent capitalization and combinations. Historical usage remains associated with these organizations. Therefore, an apparently obsolete LCom Organization remains an important part of historical account identity and cannot simply be excluded from the account universe.

## Salesforce Accounts

Salesforce represents primarily the **commercial side** of the organization.

Salesforce contains Accounts for educational organizations regardless of whether they currently have revenue, technical support cases, training sessions, licenses, or product usage. Opportunities and other Salesforce objects can be associated with Accounts at different levels.

For public education, the natural hierarchy is generally:

```text
District / Ultimate Parent
   ├── School
   ├── School
   └── School
```

For private organizations and other account types, Salesforce can contain multiple intermediate levels between the lowest-level organization and the Ultimate Parent.

Opportunities are preferably maintained at the district level for public schools, but this is not enforced consistently. Revenue can therefore exist at a school, district, intermediate organization, or Ultimate Parent. A single account at the district level can also have some opportunities associated with the district and others associated directly with individual schools.

For Learning.com business reporting, the agreed definition of a **Customer is the Salesforce Ultimate Parent Account**. Thus several schools with separate opportunities under the same district still constitute one Customer.

### Salesforce Ownership

Every individual Salesforce Account can have its own Account Owner. Owners are therefore attributes of individual accounts rather than inherently of the entire hierarchy.

However, analysis of the current account data in August 2026 showed that ownership is highly consistent across commercially relevant hierarchies. Among accounts with contracts, differences between the individual Account Owner and the Ultimate Parent Account Owner were extremely rare—approximately **0.2%** in the analyzed data.

Therefore, the **Ultimate Parent Account Owner can practically serve as the conformed Customer Owner** for customer-level reporting, while the individual Account Owner should remain available when account-level ownership is required.


## Account Origins and Integrations

Salesforce is the current master system of record for commercial account information, but it is not necessarily the original point of creation for every Account.

Accounts can originate in **HubSpot** and subsequently be moved/synchronized into Salesforce through the HubSpot–Salesforce integration.

Salesforce is also integrated with **NetSuite**. It is theoretically possible that an organization could originate through the NetSuite side and subsequently become represented in Salesforce, although it is not currently known whether this occurs in practice.

Therefore, "Salesforce Account" describes the organization's commercial identity in the current system of record but does not necessarily imply that the entity was originally created in Salesforce.

## Historical Evolution

LCom license and usage history extends to 2020 and earlier.

Before approximately 2024, commercial information was maintained exclusively in NetSuite and was subsequently imported into Salesforce. Since that migration, Salesforce has been the commercial master system.

This creates an important distinction in data quality. Older imported Accounts and relationships can contain more inconsistencies. Processes after 2024 impose more structure, but the rules are still not sufficiently strong to prevent incorrect hierarchy assignments, duplicate Accounts, missing relationships, or other inconsistencies.

Account and hierarchy data change over time, but reporting generally uses the current organization, hierarchy, and ownership as the best available representation. Historical changes are retained in the data warehouse from May 2025, primarily for traceability rather than historical account reporting.

## Relationship Between LCom Organizations and Salesforce Accounts

LCom Organizations and Salesforce Accounts do not share a naturally enforced common identifier.

Their relationship is established operationally and can occur after either record has already been created. An organization may first appear in LCom or Salesforce and be linked later.

The current data consequently contains:

- organizations successfully represented and linked in both systems;
- LCom-only organizations;
- Salesforce-only Accounts;
- similar organizations in both systems without a recognized link;
- duplicates;
- potentially incorrect historical links;
- disagreements about organizational level between the systems.

A Salesforce school can, for example, be linked to something represented as a district in LCom, or vice versa.

These disagreements do not necessarily mean that one entire source hierarchy is wrong. The systems describe organizations for different purposes.

## External Educational Reference Data and Terminology

Public educational organization data from **NCES** is periodically loaded into Salesforce and is available as attributes on the Account object. This provides another source of descriptive information about public schools and districts, but it does not replace the operational LCom hierarchy or the commercial Salesforce hierarchy.

Business terminology is not always used consistently. In internal conversations, a **school** may be referred to as a **building**, while a **district** may sometimes be referred to simply as an **account** or **customer**. These are conversational terms rather than precise hierarchy definitions. In particular, the formal reporting definition of **Customer** remains the Salesforce Ultimate Parent Account.

The term *building* may come from public-education terminology such as NCES data or from licensing concepts such as licenses per building rather than per individual student.

## Customers vs. License-Holding and Usage Accounts

Most customers came from **District Deal** paying for and using LCom products themselve. Those customers generate revenue, hold licenses and generate usage.

A particularly important distinction is that the **State Program Deal** customers pay for  LCom products but not necessarily use  LCom products.

A state Department of Education can hold the Salesforce contract and revenue, while individual districts receive licenses and generate usage:

```text
State Department of Education
        │
        │ commercial contract / revenue
        │
        ├── District A → licenses → schools → usage
        ├── District B → licenses → schools → usage
        └── District C → licenses → schools → usage
```

Those districts can legitimately have licenses and substantial usage with $0 district-level Salesforce contracts and revenue. Conversely, a State Program Deal account can have non-zero revenue but no corresponding LCom licenses or usage. In State Program Deals, Salesforce opportunities with monetary amounts provide the commercial basis for licenses to be created for eligible districts and schools.

Salesforce contains a manually maintained flag indicating whether an Account—at either school or district level—is eligible to consume licenses and generate usage under a State Program Deal. The flag can be turned off when there is no currently active State Program Deal.

However, the eligibility flag does **not** establish a physical relationship between an eligible Account and the Salesforce Account or Opportunity that funds it. For large State Program Deals, the relationship is generally understood from business knowledge: eligible districts and schools are expected to be in the state whose Department of Education purchased the program, and the relevant state deal is widely known within the organization. This relationship is not represented by a direct Salesforce Account or Opportunity attribute.

For smaller or more complex deals, the method used to determine eligibility is less clear and may depend primarily on operational or institutional knowledge. Such relationships may not necessarily be represented by the State Program eligibility flag at all. Consequently, the flag is more directly useful for analyzing **license and usage eligibility** than for establishing a reliable revenue-to-consuming-account relationship.

State Departments of Education are the largest contributors to State Program Deal revenue, but similar umbrella relationships can also exist between other organizations, including commercial educational organizations with more complex structures.

Commercial relationships can also overlap. An organization can hold a State Program Deal that funds licenses for other organizations while also having separate opportunities that fund its own licenses or usage. Likewise, a district or school covered by a State Program Deal can also have its own opportunities for other products, services, or additional coverage. The exact business interpretation of these mixed deal patterns cannot always be determined from Account attributes alone; some of the meaning is derived from Opportunity deal types and organizational knowledge.

Trials and demos introduce further legitimate combinations: an organization can have trial/demo licenses or usage without a commercial Salesforce Account, or can have a corresponding trial/demo commercial record with $0 district-level Salesforce contracts and revenue.

Therefore:

> **Revenue, license ownership, and product usage are related aspects of an organization, but none of them individually defines the role of the organization and the level it occupies.**

## The Practical Organizational Hierarchy

For analytical purposes, the organization can be viewed through three business roles:

```text
Account / Organization
        ↓
District / Operating Parent
        ↓
Customer / Ultimate Commercial Parent
```

Or, when starting from the typical lowest public-education level:

```text
School → District → Customer
```

These are **roles**, not necessarily three different physical organizations.

A district can occupy both Account and District roles:

```text
District X → District X → Customer Y
```

A public-school district that is itself the ultimate commercial Customer can occupy all three:

```text
District X → District X → District X
```

A school normally occupies only the lowest role:

```text
School A → District X → District X
```

And private organizations can have structures that do not correspond literally to public-school terminology.

The LCom hierarchy is generally the stronger representation of the **operational school/district relationship**, because that hierarchy governs licenses and product usage. Salesforce Ultimate Parent is the stronger representation of the **commercial Customer relationship**, because Salesforce governs opportunities and revenue.

## Core Interpretation of the Account Entity

The most useful overall definition is therefore:

> **An Account is the conformed representation of an organization that has, had, or may have a commercial, licensing, organizational, or product-usage relationship with Learning.com. The organization may originate in LCom Platform, Salesforce, or an integrated upstream system and may exist in only one system. Its operational hierarchy and commercial hierarchy can differ: LCom provides the primary view of school/district product organization, while Salesforce provides the primary view of commercial Customer/Ultimate Parent. Individual accounts can have their own Salesforce owners, while the Ultimate Parent owner provides a practical conformed Customer Owner. Historical, deleted, unlinked, duplicate, generic, and source-only organizations remain part of the account domain when required to preserve historical revenue, licensing, or usage activity.**

The central complication of the entity is therefore not merely duplicate matching. **Learning.com has overlapping operational and commercial representations of the same organizational world, created at different times for different purposes and with different hierarchy rules.** A usable account model has to preserve both rather than assume that either Salesforce or LCom alone completely defines what an Account is.

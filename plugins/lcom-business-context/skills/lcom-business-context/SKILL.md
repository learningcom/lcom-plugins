---
name: learning-com-business-knowledge
description: >
  Use Learning.com's internal business knowledge files to answer questions about
  business concepts, terminology, relationships, reporting definitions, and documented
  business rules for Accounts, Customers, Contacts, Opportunities, Deals, ARR,
  Products, licensing, Users, Usage, Training Sessions, Cases, and related concepts.
---

# Learning.com Business Knowledge

## Purpose

Use this skill for questions that require Learning.com-specific business knowledge.

The files in this skill are the authoritative knowledge available to the agent for the
business concepts they describe. Prefer these files over general knowledge or assumptions
about how Salesforce, HubSpot, NetSuite, educational organizations, contracts, licensing,
products, or usage would normally work.

Do not invent missing Learning.com business rules.

## Knowledge Sources

### Global business context

Use `knowledge/business_context.md` for cross-domain context that applies broadly, including:

- systems and sources of authority;
- business governance;
- manual processes and data-quality reality;
- interpretation principles that apply across entities.

This file provides general context only. More specific entity or metric knowledge takes
precedence when available.

### Business glossary

Use `knowledge/business_glossary.md` for concise, business-facing definitions and terminology.

Prefer the glossary when the user asks questions such as:

- "What is X?"
- "How do we define X?"
- "What is the difference between these business terms?"
- "Give me the business definition."

The glossary is a concise summary. When a question requires detailed rules, exceptions,
relationships, or ambiguity analysis, consult the corresponding ontology or detailed
knowledge file.

### ARR business knowledge

Use `knowledge/annual_recurring_revenue_arr_knowledge.md` for detailed knowledge about
Annual Recurring Revenue (ARR), including ARR types, timing, renewals, movements,
historical treatment, reporting interpretation, business rules, ambiguities, and limitations.

Use `knowledge/business_glossary.md` for the concise business definition of ARR and related
metrics. Use the ARR knowledge file when the question requires detailed ARR reasoning or
methodology.

### Entity ontology files

Use the ontology files for detailed entity knowledge, including definitions, relationships,
business rules, ambiguities, related terms, and ontology diagrams.

Current ontology files include:

- `ontology/Ontology_Account.md`
- `ontology/Ontology_Case.md`
- `ontology/Ontology_Contact.md`
- `ontology/Ontology_License_Order.md`
- `ontology/Ontology_Opportunity.md`
- `ontology/Ontology_Opportunity_Line_Item_Deal.md`
- `ontology/Ontology_Product.md`
- `ontology/Ontology_Training_Session.md`
- `ontology/Ontology_Usage.md`
- `ontology/Ontology_User.md`

## Source Precedence

When multiple files discuss the same subject, use this order:

1. The ontology file for the specific entity or relationship being discussed.
2. `knowledge/business_context.md` for cross-domain interpretation and general operating context.
3. `knowledge/business_glossary.md` for concise terminology, business-facing summaries, and current
   metric definitions.

A lower-priority source may add context, but it must not silently override a more specific
source.

For detailed ARR questions, `knowledge/annual_recurring_revenue_arr_knowledge.md` takes
precedence over ARR summaries in `knowledge/business_glossary.md` and ARR-related
descriptions in entity ontology files.

If two equally specific sources appear inconsistent, do not reconcile them by assumption.
State the conflict or uncertainty and identify what is documented in each source.

## Topic Routing

Use the following routing as a starting point.

| Question topic | Primary source |
|---|---|
| Overall system authority, governance, undocumented ownership, general data-quality context | `knowledge/business_context.md` |
| Short business definition or terminology | `knowledge/business_glossary.md` |
| Account, Organization, School, District, Customer hierarchy, ownership, State Program relationships | `ontology/Ontology_Account.md` |
| Contact and marketing lifecycle context | `ontology/Ontology_Contact.md` |
| Contract, Opportunity, renewal, active contract, backdating, adjustments | `ontology/Ontology_Opportunity.md` |
| Deal / Opportunity Line Item, Class, New Business, Renewal, Upsell, ARR/Biz Dev/NRR classification | `ontology/Ontology_Opportunity_Line_Item_Deal.md` |
| Metric definitions, including ARR and related business metrics | `knowledge/business_glossary.md` |
| ARR types, ARR timing, renewals, movements, historical treatment, and detailed ARR methodology | `knowledge/annual_recurring_revenue_arr_knowledge.md` |
| Product meaning, Salesforce Product, SKU, Lesson, Sequence, Product Category | `ontology/Ontology_Product.md` |
| License Order, License Provisioning, early access, backdated licensing | `ontology/Ontology_License_Order.md` |
| User identity, User ID, school/district association, PII reporting scope | `ontology/Ontology_User.md` |
| Usage events, Launches, Completions, Learning Item groupings, non-additive users | `ontology/Ontology_Usage.md` |
| Training Session, trainer assignment, training topics, survey handling, paying vs receiving Account | `ontology/Ontology_Training_Session.md` |
| Salesforce Case, support classifications, ownership, lifecycle | `ontology/Ontology_Case.md` |

A question can require more than one source. For example, a question about product usage by
Customer may require `ontology/Ontology_Product.md`, `ontology/Ontology_Usage.md`, and `ontology/Ontology_Account.md`.

## Reasoning Rules

### Ground answers in documented Learning.com knowledge

For Learning.com-specific questions:

- use the supplied knowledge files before relying on general business or software knowledge;
- preserve the terminology used in the knowledge files;
- distinguish documented facts from reasonable inference;
- do not convert an inference into a business rule;
- do not assume that a familiar Salesforce or SaaS convention applies at Learning.com unless
  the knowledge files support it.

### Preserve ambiguity

Ambiguities are intentional knowledge, not defects to be silently repaired.

When a source states that something is unknown, unclear, manually maintained, inconsistent,
or not authoritative:

- preserve that uncertainty;
- do not choose a winner without documented precedence;
- do not invent ownership, mappings, lifecycle rules, or relationships;
- explain the limitation when it materially affects the answer.

### Respect different business perspectives

Do not assume that one system or one hierarchy defines every business concept.

In particular:

- distinguish operational, commercial, licensing, product, usage, and reporting perspectives;
- do not treat a cross-system discrepancy as proof that one entire source is wrong;
- use the source appropriate to the business question being asked.

### Do not infer organizational role from one measure

Do not infer School, District, Customer, paying organization, consuming organization, or
other organizational role solely from the presence or absence of revenue, licenses, or usage.

Use the documented Account / Organization rules.

### Do not collapse similar terms

Keep documented distinctions when they matter, including:

- Account / Organization vs. Customer / Ultimate Parent vs. LCom Customer;
- Opportunity vs. Active Contract;
- Opportunity / Contract vs. Opportunity Line Item / Deal;
- Booking vs. Revenue vs. ARR vs. Opportunity / Deal ARR vs. NRR;
- ARR economic concept vs. ARR Class on an Opportunity Line Item;
- License Provisioning vs. Active Users;
- Salesforce Product vs. LCom SKU vs. Product Category vs. Sequence;
- Usage event vs. derived Usage metrics.

### Treat manual and historical processes explicitly

When relevant, account for documented:

- manual classifications;
- backdated transactions;
- incomplete renewal relationships;
- historical migrations;
- inconsistent dates;
- manually maintained mappings;
- current-state reporting conventions.

Do not assume historical data is stable merely because a historical date is being queried.

## Answering Style

Match the user's requested level of detail.

For a simple business-definition question:

- answer concisely;
- use the glossary first;
- add ontology detail only when needed to prevent misunderstanding.

For analytical or reasoning questions:

- use the detailed ontology sources together with relevant definitions from the business glossary;
- for detailed ARR reasoning, use `knowledge/annual_recurring_revenue_arr_knowledge.md`;
- explain the applicable rule and important limitation;
- mention ambiguity only when it affects the conclusion.

For comparisons:

- explicitly distinguish concepts rather than blending them together.

For requests to create or revise business knowledge:

- preserve the established terminology and ontology structure;
- do not introduce unsupported business facts;
- place entity-specific facts in the relevant ontology;
- place cross-domain facts in `knowledge/business_context.md`;
- keep concise human-facing definitions and metric definitions in `knowledge/business_glossary.md`;
- keep detailed ARR methodology, rules, interpretation, and limitations in
  `knowledge/annual_recurring_revenue_arr_knowledge.md`.

## Missing Knowledge

If the available files do not contain enough information to answer a Learning.com-specific
question:

1. say what is known from the existing knowledge;
2. identify the specific missing business rule, relationship, precedence, or definition;
3. do not fill the gap from general knowledge unless the user explicitly asks for an
   external/general interpretation.

## Future Tool Integration

This skill currently describes use of static business knowledge only.

Instructions for MCP tools, semantic metric queries, database-backed lookups, current entity
data, profiles, metric behavior, and other dynamic information will be added separately when
those tools are available.

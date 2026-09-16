# Account

An **Account / Organization** represents a public or commercial educational organization that has, had, or may have a relationship with Learning.com. This can include schools, districts, state education organizations, private schools, and other organizations that purchase products, hold licenses, use Learning.com products, receive services, or exist as prospects.

An Account has both an **operational** and a **commercial** context, and these do not always align. Operationally, schools and districts represent where licenses and product usage occur. Commercially, revenue can be assigned to any level of account hierarchy.

- A typical public-education structure is **School → District**.
- Commercial organizations are grouped under a **Customer**, defined as the **Salesforce Ultimate Parent Account**. They may have additional intermediate levels, but for reporting purposes the hierarchy is represented as **School → District → Customer**.
- An individual low-level account such as a school is not counted as a company customer even if revenue is associated directly with that school; it is reported under its parent account like District or Customer along with other schools in this district.
- Most accounts both pay for and use Learning.com products, but some arrangements—particularly **State Program Deals**—have one account (like a State Department of Education) paying while other accounts (public districts and schools) receive licenses and generate usage.
- Licenses are always provisioned at the District level
- Product Usage mostly collected at the School level with small amount at the District level when a school can not be defined from the data
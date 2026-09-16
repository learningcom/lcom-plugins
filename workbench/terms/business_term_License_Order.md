# License Order

A **License Order** represents licensing for an LCom District for a defined period and LCom Product. It is created from a **Salesforce Opportunity Line Items** and includes **License Provisioning**, usually expressed as a number of students, along with the schools covered by the order. License Provisioning represents how many students Learning.com is paid to serve and is an estimate of potential student use rather than a limit on how many individual users may access the platform.

**License Provisioning should not be confused with Active Users.** Active Users are users, mostly students, who have actually started using the LCom Platform. Because the provisioned quantity does not limit access, actual users can exceed License Provisioning. Provisioning is maintained for the District-level order and is not allocated to individual schools, so it cannot be used to determine accurate school-level provisioning or utilization.

- License Orders have Start and End dates and may be enforced or unenforced.
- Late-closing contracts can create backdated License Orders and change historical active-license counts.
- License Orders may be manually unenforced to provide early access while a late-payment renewal is unresolved.
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
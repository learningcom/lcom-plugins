# LCom Customer

An **LCom Customer** is an organization at the **Customer / Ultimate Parent level** with **non-zero ARR from active contracts**. It represents the organization counted as a customer when answering business questions such as **“How many customers does Learning.com have?”**

Revenue may come from contracts associated with different Accounts within the Customer hierarchy. Individual Accounts—such as schools or Accounts in the District role—are **not counted as separate LCom Customers**, even when they have their own active contracts and non-zero ARR. Their revenue contributes to their Customer / Ultimate Parent.

- When an LCom Customer’s total ARR becomes **$0**, the Customer is considered **churned**.
- Holding licenses or using Learning.com products does **not** make an organization an LCom Customer.
- Districts and schools using products through a **State Program Deal** are license holders/product users, not separate LCom Customers, unless they belong to a different Customer / Ultimate Parent with its own non-zero ARR.
- Because these license holders are not LCom Customers, losing their State Program access or usage is **not customer churn**.
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

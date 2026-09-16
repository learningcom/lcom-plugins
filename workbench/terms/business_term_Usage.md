# Usage

**Usage** represents interactions by Users with Learning Items in the LCom Platform, such as launching or completing a lesson. Each Usage event is associated with a User, a Learning Item, a Grade, and an organization—normally a School, or a District when the School is not available.

Learning Items can be organized in several independent ways, including Topic, SKU, Sequence, Unit, Default Path, and Product Category. These groupings do not form a single hierarchy, and a specific Usage event cannot be reliably tied to the particular licensed SKU or Salesforce Product that provided access.

- The same User may launch or complete the same Learning Item more than once.
- Product Categories can overlap because a Learning Item may belong to more than one category, so totals across categories are not additive.
- Unique User counts are also non-additive across organizational levels. Summing School-level unique Users is accepted as an approximation for higher levels, with an observed difference of approximately 2% or less from the exact distinct count.
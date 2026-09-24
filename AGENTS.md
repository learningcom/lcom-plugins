## Learning.com Metrics

For questions requiring business metric values, use the `lcom_metrics` MCP server instead of generating SQL.

Before querying metrics:

1. Use `get_metrics` to identify the exact metric name.
2. Use `get_dimensions` to identify valid dimensions.
3. Use controlled-value tools such as `get_state_codes` or `get_countries` when those dimensions are filtered.
4. Execute the metric using `run_metricflow_query`.

Do not invent metric names, dimensions, or controlled dimension values.

If `run_metricflow_query` returns `success: false`, use the returned validation error to correct the MCP query and retry.

## Learning.com Account Context

For questions about a specific Account / Organization, such as:

- "Explain account XYZ."
- "How is account XYZ doing?"
- "Tell me about school XYZ."
- "Draw a knowledge graph for account XYZ."

use the `get_account` tool from the `lcom_metrics` MCP server instead of generating SQL along with all available metrics for account__name dimension if school and account__district_name if district

The `get_account` tool accepts:

- `account_name` — required partial Account / Organization name.
- `state_code` — optional state code used to narrow account matches.
- `district_name` — optional district name, primarily used to distinguish schools with similar or identical names.

Account names are not unique.

If `get_account` returns multiple matches:

1. Do not arbitrarily select an account.
2. Present the matching account names, states, and districts to the user.
3. If the matches are in different states, ask the user to clarify the state.
4. Use `get_state_codes` to determine the valid state-code value before calling `get_account` again.
5. If multiple schools still match within the selected state, ask the user to clarify the district.
6. Call `get_account` again using the clarified `account_name`, `state_code`, and, when necessary, `district_name`.
7. Do not ask the user for internal Account IDs.

If exactly one account is returned, use the structured Account data to explain the organization, assess its available activity, or construct a knowledge graph.

Warehouse default values must not be interpreted as actual business values:

- `Unknown` means the source value is missing or unavailable.
- `1900-01-01` means the date value is missing or unavailable.

Do not invent missing Account attributes, relationships, or business activity.

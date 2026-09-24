"""
Integration/regression tests for metricflow_query.

These tests validate only the query outcome contract:
- valid queries must return success=True
- invalid parameters must return success=False with validation_error

They intentionally do NOT assert exact metric values.

Because valid cases execute MetricFlow queries, the normal dbt/MetricFlow
environment and database connectivity must be available when running them.
"""

import pytest

from metricflow_mcp import MAX_QUERY_LIMIT, metricflow_query


VALID_CASES = [
    pytest.param(
        {"metrics": ["arr"]},
        id="01_valid_single_metric",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "group_by": ["account__state_code"],
            "limit": 10,
        },
        id="02_valid_group_by",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "group_by": ["account__state_code"],
            "where": "{{ Dimension('account__state_code') }} = 'CA'",
        },
        id="05_valid_state_filter",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "where": "{{ Dimension('account__country') }} = 'United States of America'",
        },
        id="07_valid_country_filter",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "where": "{{ Dimension('account__state_code') }} IN ('CA', 'TX', 'NY')",
        },
        id="09_valid_in_filter",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "start_time": "2026-06-01",
            "end_time": "2026-06-30",
        },
        id="11_valid_time_range",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "group_by": ["account__state_code"],
            "order": ["-arr"],
            "limit": 10,
        },
        id="14_valid_order",
    ),
    pytest.param(
        {
            "metrics": ["arr", "active_users"],
            "group_by": ["account__state_code"],
            "limit": 10,
        },
        id="18_multiple_metrics_common_dimension",
    ),
]


INVALID_CASES = [
    pytest.param(
        {"metrics": ["arrr"]},
        id="03_invalid_metric",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "group_by": ["account__bad_dimension"],
        },
        id="04_invalid_group_by",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "where": "{{ Dimension('account__state_code') }} = 'California'",
        },
        id="06_invalid_state_value",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "where": "{{ Dimension('account__country') }} = 'USA'",
        },
        id="08_invalid_country_value",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "where": "{{ Dimension('account__bad_dimension') }} = 'CA'",
        },
        id="10_invalid_where_dimension",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "start_time": "June 1, 2026",
            "end_time": "2026-06-30",
        },
        id="12_invalid_date_format",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "start_time": "2026-07-01",
            "end_time": "2026-06-30",
        },
        id="13_invalid_time_range",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "group_by": ["account__state_code"],
            "order": ["account__country"],
        },
        id="15_invalid_order",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "limit": 0,
        },
        id="16_invalid_limit_zero",
    ),
    pytest.param(
        {
            "metrics": ["arr"],
            "limit": MAX_QUERY_LIMIT + 1,
        },
        id="17_limit_too_large",
    ),
    pytest.param(
        {
            "metrics": ["arr", "active_users"],
            "group_by": ["arr__mon_lastday"],
        },
        id="19_dimension_not_common_to_metrics",
    ),
]


@pytest.mark.parametrize("query_args", VALID_CASES)
def test_valid_metricflow_queries(query_args):
    """Valid parameter combinations must complete successfully."""
    result = metricflow_query(**query_args)

    assert result["success"] is True, (
        f"Expected successful query, got: {result}"
    )
    assert result["error"] is None
    assert isinstance(result["data"], list)


@pytest.mark.parametrize("query_args", INVALID_CASES)
def test_invalid_metricflow_queries(query_args):
    """Invalid parameters must be rejected by our validation layer."""
    result = metricflow_query(**query_args)

    assert result["success"] is False, (
        f"Expected validation failure, got: {result}"
    )
    assert result["data"] is None
    assert result["error"] is not None
    assert result["error"]["type"] == "validation_error", (
        f"Expected validation_error, got: {result['error']}"
    )
    assert result["error"]["message"]

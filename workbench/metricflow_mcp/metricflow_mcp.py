import os
from pathlib import Path
from typing import Any

import pandas as pd
from dotenv import load_dotenv
from fastmcp import FastMCP

from dbt_metricflow.cli.cli_configuration import CLIConfiguration
from metricflow.engine.metricflow_engine import MetricFlowQueryRequest

from datetime import datetime
import re
import yaml

from decimal import Decimal
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# =========================================================
# Environment
# =========================================================

load_dotenv()

DBT_PROJECT_DIR = Path(os.environ["DBT_PROJECT_DIR"])
DBT_PROFILES_DIR = Path(os.environ["DBT_PROFILES_DIR"])
DBT_TARGET = os.environ["DBT_TARGET"]


# =========================================================
# MCP Server
# =========================================================

mcp = FastMCP("LCom Metrics Server")

MAX_QUERY_LIMIT = 100
# =========================================================
# Temporary controlled dimension values
# Later these will be retrieved from the database.
# =========================================================






# =========================================================
# Exceptions
# =========================================================

class QueryValidationError(Exception):
    """
    Raised when a semantic query parameter fails validation.
    """
    # TBD
    pass

# =========================================================
# Account data
# =========================================================

def account_query(
    account_name: str,
    state_code: str | None = None,
    district_name: str | None = None,
) -> dict[str, Any]:
    """
    Find an Account / Organization in semantic.vws_account.

    account_name:
        Required partial account name. Matching uses ILIKE '%name%'.

    state_code:
        Optional state code used to narrow account matches.
        Must be one of the values returned by get_valid_state_codes().

    district_name:
        Optional partial district name used primarily to distinguish
        schools with similar or identical names.

    Returns:
        status = "not_found"
            No matching accounts.

        status = "multiple_matches"
            More than one account matched. Candidate names, states,
            districts, customers, and account types are returned so the
            AI can ask the user to clarify the organization.

        status = "ok"
            Exactly one account matched and the complete Account context
            is returned.
    """

    try:
        # -----------------------------------------------------
        # Validate parameters
        # -----------------------------------------------------

        if not account_name or not account_name.strip():
            raise QueryValidationError(
                "account_name must be provided."
            )

        if state_code:
            state_code = state_code.upper()

            valid_state_codes = get_valid_state_codes()

            if state_code not in valid_state_codes:
                raise QueryValidationError(
                    f"Invalid state_code '{state_code}'. "
                    f"Valid state codes are: {valid_state_codes}"
                )

        # -----------------------------------------------------
        # Get current dbt target connection information
        # -----------------------------------------------------

        profiles_path = DBT_PROFILES_DIR / "profiles.yml"

        with open(profiles_path, "r", encoding="utf-8") as f:
            profiles = yaml.safe_load(f)

        profile = profiles["LCom_DW"]

        if DBT_TARGET not in profile["outputs"]:
            raise QueryValidationError(
                f"DBT target '{DBT_TARGET}' was not found "
                f"in profile 'LCom_DW'."
            )

        target_config = profile["outputs"][DBT_TARGET]

        connection_url = URL.create(
            drivername="redshift+psycopg2",
            username=target_config["user"],
            password=target_config["password"],
            host=target_config["host"],
            port=target_config.get("port", 5439),
            database=target_config["dbname"],
        )

        engine = create_engine(connection_url)

        # -----------------------------------------------------
        # Build query
        # -----------------------------------------------------

        where = [
            "name ILIKE :account_name"
        ]

        params = {
            "account_name": f"%{account_name.strip()}%"
        }

        if state_code:
            where.append("state_code = :state_code")
            params["state_code"] = state_code

        if district_name:
            where.append(
                "district_name ILIKE :district_name"
            )
            params["district_name"] = f"%{district_name.strip()}%"

        sql = text(
            f"""
            SELECT
                account_id,
                name,

                conformed_district_id,
                district_name,
                conformed_customer_id,
                customer_name,

                account_type,
                customer_level,

                country,
                state_code,
                state_name,
                county,
                urban_rural,
                enrollment,

                owner_id,
                owner,

                sfdc_account_id,
                sfdc_name,
                sfdc_parent_id,
                sfdc_parent_name,
                sfdc_ultimate_parent_id,
                sfdc_ultimate_parent_account,

                lcom_organization_id,
                lcom_organization_name,
                lcom_organization_type,
                lcom_parent_organization_id,
                lcom_parent_organization_name,
                lcom_nces_id,
                lcom_external_sis_id,

                state_initiative,
                sfdc_state_program_eligible,
                lcom_trial,
                lcom_demo,

                has_product_licenses,
                has_product_usage,

                total_won_opportunities,
                total_open_opportunities,
                first_invoiced_date,
                latest_start_date,
                latest_end_date,
                latest_open_opportunities_modified_date,

                total_won_deals,
                total_won_state_program_deals,

                total_training_sessions,
                latest_training_session_on,

                total_cases,
                currently_open_cases,
                latest_case_created_date,
                latest_open_case_modified_date

            FROM semantic.vws_account

            WHERE {" AND ".join(where)}

            ORDER BY
                state_code,
                district_name,
                name
            LIMIT {MAX_QUERY_LIMIT}
            """
        )

        # -----------------------------------------------------
        # Execute
        # -----------------------------------------------------

        try:
            with engine.connect() as connection:
                result = connection.execute(sql, params)
                rows = [
                    dict(row)
                    for row in result.mappings().all()
                ]
        finally:
            engine.dispose()

        # -----------------------------------------------------
        # Make returned values JSON-safe
        # -----------------------------------------------------

        def json_value(value):
            if isinstance(value, (datetime,)):
                return value.isoformat()

            if hasattr(value, "isoformat"):
                return value.isoformat()

            if isinstance(value, Decimal):
                return float(value)

            return value

        rows = [
            {
                key: json_value(value)
                for key, value in row.items()
            }
            for row in rows
        ]

        # -----------------------------------------------------
        # No matches
        # -----------------------------------------------------

        if not rows:
            return {
                "success": True,
                "status": "not_found",
                "match_count": 0,
                "search": {
                    "account_name": account_name,
                    "state_code": state_code,
                    "district_name": district_name,
                },
                "data": None,
                "error": None,
            }

        # -----------------------------------------------------
        # Multiple matches
        #
        # Return only attributes useful for human
        # disambiguation.
        # -----------------------------------------------------

        if len(rows) > 1:
            return {
                "success": True,
                "status": "multiple_matches",
                "requires_disambiguation": True,
                "match_count": len(rows),
                "search": {
                    "account_name": account_name,
                    "state_code": state_code,
                    "district_name": district_name,
                },
                "data": {
                    "candidates": [
                        {
                            "name": row["name"],
                            "state_code": row["state_code"],
                            "district_name": row["district_name"],
                            "customer_name": row["customer_name"],
                            "account_type": row["account_type"],
                        }
                        for row in rows
                    ]
                },
                "error": None,
            }

        # -----------------------------------------------------
        # Exactly one account
        # -----------------------------------------------------

        row = rows[0]

        return {
            "success": True,
            "status": "ok",
            "match_count": 1,

            "data": {
                "account": {
                    "account_id": row["account_id"],
                    "name": row["name"],
                    "account_type": row["account_type"],
                    "customer_level": row["customer_level"],
                    "country": row["country"],
                    "state_code": row["state_code"],
                    "state_name": row["state_name"],
                    "county": row["county"],
                    "urban_rural": row["urban_rural"],
                    "enrollment": row["enrollment"],
                },

                "hierarchy": {
                    "district": {
                        "account_id": row["conformed_district_id"],
                        "name": row["district_name"],
                    },
                    "customer": {
                        "account_id": row["conformed_customer_id"],
                        "name": row["customer_name"],
                    },
                },

                "ownership": {
                    "owner_id": row["owner_id"],
                    "owner": row["owner"],
                },

                "source_identity": {
                    "salesforce": {
                        "account_id": row["sfdc_account_id"],
                        "name": row["sfdc_name"],
                        "parent_id": row["sfdc_parent_id"],
                        "parent_name": row["sfdc_parent_name"],
                        "ultimate_parent_id":
                            row["sfdc_ultimate_parent_id"],
                        "ultimate_parent_name":
                            row["sfdc_ultimate_parent_account"],
                    },

                    "lcom": {
                        "organization_id":
                            row["lcom_organization_id"],
                        "organization_name":
                            row["lcom_organization_name"],
                        "organization_type":
                            row["lcom_organization_type"],
                        "parent_organization_id":
                            row["lcom_parent_organization_id"],
                        "parent_organization_name":
                            row["lcom_parent_organization_name"],
                        "nces_id":
                            row["lcom_nces_id"],
                        "external_sis_id":
                            row["lcom_external_sis_id"],
                    },
                },

                "programs": {
                    "state_initiative":
                        row["state_initiative"],
                    "state_program_eligible":
                        row["sfdc_state_program_eligible"],
                    "trial":
                        row["lcom_trial"],
                    "demo":
                        row["lcom_demo"],
                },

                "product_activity": {
                    "has_product_licenses":
                        row["has_product_licenses"],
                    "has_product_usage":
                        row["has_product_usage"],
                },

                "commercial_activity": {
                    "total_won_opportunities":
                        row["total_won_opportunities"],
                    "total_open_opportunities":
                        row["total_open_opportunities"],
                    "first_invoiced_date":
                        row["first_invoiced_date"],
                    "latest_start_date":
                        row["latest_start_date"],
                    "latest_end_date":
                        row["latest_end_date"],
                    "latest_open_opportunities_modified_date":
                        row[
                            "latest_open_opportunities_modified_date"
                        ],
                    "total_won_deals":
                        row["total_won_deals"],
                    "total_won_state_program_deals":
                        row["total_won_state_program_deals"],
                },

                "training": {
                    "total_training_sessions":
                        row["total_training_sessions"],
                    "latest_training_session_on":
                        row["latest_training_session_on"],
                },

                "support": {
                    "total_cases":
                        row["total_cases"],
                    "currently_open_cases":
                        row["currently_open_cases"],
                    "latest_case_created_date":
                        row["latest_case_created_date"],
                    "latest_open_case_modified_date":
                        row["latest_open_case_modified_date"],
                },
            },

            "error": None,
        }

    except QueryValidationError as error:
        return validation_error_response(error)

    except Exception as error:
        return {
            "success": False,
            "status": "error",
            "data": None,
            "error": {
                "type": "account_query_error",
                "message": str(error),
            },
        }


# =========================================================
# MetricFlow
# =========================================================

def create_metricflow_engine():
    """
    Initialize and return the MetricFlow engine using
    DBT_PROJECT_DIR, DBT_PROFILES_DIR and DBT_TARGET.
    """

    # MetricFlow/dbt uses this environment variable
    # to select the dbt target.
    os.environ["DBT_TARGET"] = DBT_TARGET

    config = CLIConfiguration()

    config.setup(
        dbt_project_path=DBT_PROJECT_DIR,
        dbt_profiles_path=DBT_PROFILES_DIR,
        configure_file_logging=False,
    )

    return config.mf

# Initialize MetricFlow once when the server starts
metricflow_engine = create_metricflow_engine()

def get_metricflow_metrics() -> list[str]:
    """
    Retrieve all currently available metric names directly from MetricFlow.

    Internal function. Not exposed as an MCP tool.
    """

    metrics = metricflow_engine.list_metrics()

    return [metric.name for metric in metrics]


def get_metricflow_dimensions(
    metrics: list[str],
) -> list[str]:

    dimensions = metricflow_engine.simple_dimensions_for_metrics(metrics)

    return [
        dimension.name
        if dimension.name == "metric_time"
        else dimension.dunder_name
        for dimension in dimensions
    ]


# =========================================================
# Validation
# =========================================================

def validate_metrics(
    metrics: list[str],
    valid_metrics: list[str],
) -> None:
    if not metrics:
        raise QueryValidationError(
            "At least one metric must be provided."
        )

    invalid_metrics = [
        metric
        for metric in metrics
        if metric not in valid_metrics
    ]

    if invalid_metrics:
        raise QueryValidationError(
            f"Invalid metric(s): {invalid_metrics}. "
            f"Valid metrics are: {valid_metrics}"
        )


def validate_group_by(
    group_by: list[str] | None,
    valid_dimensions: list[str],
) -> None:

    if not group_by:
        return

    invalid_dimensions = [
        dimension
        for dimension in group_by
        if dimension not in valid_dimensions
    ]

    if invalid_dimensions:
        raise QueryValidationError(
            f"Invalid group-by dimension(s): {invalid_dimensions}. "
            f"Valid dimensions are: {valid_dimensions}"
        )


def validate_where(
    where: str | None,
    valid_dimensions: list[str],
) -> None:
    """
    Validate dimensions and controlled dimension values used
    in the MetricFlow where expression.

    Validates:
      - dimension names
      - dimension availability
      - state_code values
      - country values
      - controlled values must be quoted strings

    Supported controlled-dimension operators:
      - =
      - !=
      - IN
      - NOT IN

    Raises:
        QueryValidationError:
            If a dimension name or controlled value is invalid.
    """

    if not where:
        return

    valid_dimension_names = set(valid_dimensions)

    # -----------------------------------------------------
    # Extract all Dimension(...) references
    #
    # Example:
    # {{ Dimension('account__state_code') }}
    # -----------------------------------------------------

    dimension_pattern = re.compile(
        r"Dimension\(\s*['\"]([^'\"]+)['\"]\s*\)"
    )

    where_dimensions = dimension_pattern.findall(where)

    if not where_dimensions:
        raise QueryValidationError(
            "The where expression does not contain a valid "
            "MetricFlow Dimension(...) reference."
        )

    # -----------------------------------------------------
    # Validate dimension names
    # -----------------------------------------------------

    invalid_dimensions = [
        dimension
        for dimension in set(where_dimensions)
        if dimension not in valid_dimension_names
    ]

    if invalid_dimensions:
        raise QueryValidationError(
            f"Invalid filter dimension(s): {invalid_dimensions}. "
            f"Valid dimensions are: {sorted(valid_dimension_names)}"
        )

    # -----------------------------------------------------
    # Validate controlled dimension values
    # -----------------------------------------------------

    def validate_controlled_dimension(
        dimension_name: str,
        valid_values: list[str],
    ) -> None:

        if dimension_name not in where_dimensions:
            return

        escaped_dimension = re.escape(dimension_name)

        found_values: list[str] = []

        # -------------------------------------------------
        # = or !=
        #
        # {{ Dimension('account__state_code') }} = 'CA'
        # -------------------------------------------------

        comparison_pattern = re.compile(
            rf"\{{\{{\s*"
            rf"Dimension\(\s*['\"]{escaped_dimension}['\"]\s*\)"
            rf"\s*\}}\}}"
            rf"\s*(?:=|!=)\s*"
            rf"(['\"])(.*?)\1",
            re.IGNORECASE,
        )

        for match in comparison_pattern.finditer(where):
            found_values.append(match.group(2))

        # -------------------------------------------------
        # IN or NOT IN
        #
        # {{ Dimension('account__state_code') }}
        # IN ('CA', 'TX')
        # -------------------------------------------------

        in_pattern = re.compile(
            rf"\{{\{{\s*"
            rf"Dimension\(\s*['\"]{escaped_dimension}['\"]\s*\)"
            rf"\s*\}}\}}"
            rf"\s*(?:IN|NOT\s+IN)\s*"
            rf"\((.*?)\)",
            re.IGNORECASE,
        )

        for match in in_pattern.finditer(where):

            raw_values = match.group(1)

            values = re.findall(
                r"['\"]([^'\"]+)['\"]",
                raw_values,
            )

            # Remove all valid quoted values and commas.
            # Anything remaining means the expression contains
            # an unsupported/unquoted value.
            remaining = re.sub(
                r"['\"][^'\"]+['\"]",
                "",
                raw_values,
            )

            remaining = remaining.replace(",", "").strip()

            if remaining:
                raise QueryValidationError(
                    f"Values for '{dimension_name}' must be "
                    f"quoted strings. Invalid expression: ({raw_values})"
                )

            found_values.extend(values)

        # -------------------------------------------------
        # Dimension exists, but syntax/value could not
        # be validated
        # -------------------------------------------------

        if not found_values:
            raise QueryValidationError(
                f"Could not validate filter for '{dimension_name}'. "
                "Use =, !=, IN, or NOT IN with quoted string values."
            )

        # -------------------------------------------------
        # Validate values against allowed values
        # -------------------------------------------------

        invalid_values = [
            value
            for value in found_values
            if value not in valid_values
        ]

        if invalid_values:
            raise QueryValidationError(
                f"Invalid value(s) for '{dimension_name}': "
                f"{invalid_values}. "
                f"Valid values are: {valid_values}"
            )

    # -----------------------------------------------------
    # Controlled dimensions
    # -----------------------------------------------------

    validate_controlled_dimension(
        "account__state_code",
        get_state_codes(),
    )

    validate_controlled_dimension(
        "account__country",
        get_countries(),
    )


def validate_time_range(
    start_time: str | None,
    end_time: str | None,
) -> None:
    """
    Validate start_time and end_time values and formats.

    Accepted examples:
        2026-06-01
        2026-06-01T00:00:00

    Raises:
        QueryValidationError:
            If either value has an invalid ISO date/datetime format,
            or if start_time is later than end_time.
    """

    def parse_time(value: str, parameter_name: str) -> datetime:
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            raise QueryValidationError(
                f"Invalid {parameter_name}: '{value}'. "
                "Use ISO format such as '2026-06-01' "
                "or '2026-06-01T00:00:00'."
            )

    start = parse_time(start_time, "start_time") if start_time else None
    end = parse_time(end_time, "end_time") if end_time else None

    if start and end and start > end:
        raise QueryValidationError(
            f"Invalid time range: start_time '{start_time}' "
            f"is later than end_time '{end_time}'."
        )


def validate_order(
    metrics: list[str],
    group_by: list[str] | None,
    order: list[str] | None,
) -> None:
    """
    Validate requested ordering fields.

    Order fields must be either:
      - one of the requested metrics
      - one of the requested group_by (dimensions) fields

    Prefix a field with "-" for descending order.

    Examples:
        ["arr"]
        ["-arr"]
        ["account__state_code", "-arr"]

    Raises:
        QueryValidationError:
            If an order field is not present in the query.
    """

    if not order:
        return

    valid_fields = set(metrics)

    if group_by:
        valid_fields.update(group_by)

    invalid_fields = []

    for field in order:
        # Remove descending-order prefix before validation
        field_name = field[1:] if field.startswith("-") else field

        if not field_name or field_name not in valid_fields:
            invalid_fields.append(field)

    if invalid_fields:
        raise QueryValidationError(
            f"Invalid order field(s): {invalid_fields}. "
            f"Order fields must be metrics or group_by (dimensions) fields included in the query. "
            f"Valid fields are: {sorted(valid_fields)}"
        )





def validate_limit(
    limit: int | None,
) -> None:
    """
    Validate the query result limit.

    Raises:
        QueryValidationError:
            If limit is less than 1 or exceeds MAX_QUERY_LIMIT.
    """

    if limit is None:
        return

    if limit < 1:
        raise QueryValidationError(
            f"Invalid limit: {limit}. Limit must be greater than 0."
        )

    if limit > MAX_QUERY_LIMIT:
        raise QueryValidationError(
            f"Invalid limit: {limit}. "
            f"Maximum allowed limit is {MAX_QUERY_LIMIT}."
        )


# =========================================================
# Response helpers
# =========================================================

def success_response(
    data: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Build the standard successful MCP response.
    """

    return {
        "success": True,
        "data": data,
        "error": None,
    }


def validation_error_response(
    error: QueryValidationError,
) -> dict[str, Any]:
    """
    Build the standard validation-error MCP response.
    """

    return {
        "success": False,
        "data": None,
        "error": {
            "type": "validation_error",
            "message": str(error),
        },
    }


def metricflow_error_response(
    error: Exception,
) -> dict[str, Any]:
    """
    Build the standard MetricFlow execution-error MCP response.
    """

    return {
        "success": False,
        "data": None,
        "error": {
            "type": "metricflow_error",
            "message": str(error),
        },
    }

def get_valid_state_codes() -> list[str]:
    """
    Return all valid values for the account__state_code dimension.
    TBD: a database query to fetch state codes
    """
    STATE_CODES = [
    'AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN',
    'KS','KY','LA','MA','MD','ME','MI','MN','MO','MP','MS','MT','NC','ND','NE','NH',
    'NJ','NM','NV','NY','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','Unknown',
    'UT','VA','VI','VT','WA','WI','WV','WY'
    ]
    return STATE_CODES

def get_valid_countries() -> list[str]:
    """
    Return all valid values for the account__country dimension.
    TBD: a database query to fetch country codes
    """
    COUNTRIES = [
    'Australia','Bahamas','Bermuda','Bolivia','Canada','Cayman Islands','China',
    'Costa Rica','Czech Republic','Ecuador','Egypt','Estonia','Guatemala',
    'Indonesia','Italy','Japan','Kenya','Kosovo','Kuwait','Montenegro','Panama',
    'Philippines','Saudi Arabia','Sint Maarten (Dutch part)','South Africa',
    'Trinidad and Tobago','United Arab Emirates','United Kingdom',
    'United States of America','Unknown','Venezuela'
   ]

    return COUNTRIES

def metricflow_query(
    metrics: list[str],
    group_by: list[str] | None = None,
    where: str | None = None,
    start_time: str | None = None,
    end_time: str | None = None,
    order: list[str] | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    """
    Validate and execute a MetricFlow query.

    Returns:
        {
            "success": True,
            "data": [...],
            "error": None
        }

        or

        {
            "success": False,
            "data": None,
            "error": {...}
        }
    """

    try:

        # -------------------------------------------------
        # Get current MetricFlow metadata once
        # -------------------------------------------------

        valid_metrics = get_metricflow_metrics()

        # -------------------------------------------------
        # Validate metrics
        # -------------------------------------------------

        validate_metrics(
            metrics=metrics,
            valid_metrics=valid_metrics,
        )

        # Metrics are valid, so now it is safe to ask
        # MetricFlow for their common dimensions.
        valid_dimensions = get_metricflow_dimensions(metrics)

        # -------------------------------------------------
        # Validate query parameters
        # -------------------------------------------------

        validate_group_by(
            group_by=group_by,
            valid_dimensions=valid_dimensions,
        )

        validate_where(
            where=where,
            valid_dimensions=valid_dimensions,
        )

        validate_time_range(
            start_time=start_time,
            end_time=end_time,
        )

        validate_order(
            metrics=metrics,
            group_by=group_by,
            order=order,
        )

        validate_limit(limit)

        # -------------------------------------------------
        # Convert validated time strings to datetime
        # -------------------------------------------------

        parsed_start_time = (
            datetime.fromisoformat(start_time)
            if start_time
            else None
        )

        parsed_end_time = (
            datetime.fromisoformat(end_time)
            if end_time
            else None
        )

        # -------------------------------------------------
        # Build MetricFlow request
        # -------------------------------------------------

        request = MetricFlowQueryRequest.create(
        metric_names=metrics,
        group_by_names=group_by or [],
        where_constraints=[where] if where else [],
        time_constraint_start=parsed_start_time,
        time_constraint_end=parsed_end_time,
        order_by_names=order or [],
        limit=limit,
        )

        # -------------------------------------------------
        # request = MetricFlowQueryRequest.create_with_random_request_id(
        #            metric_names=metrics,
        #            group_by_names=group_by or [],
        #            where_constraint=where,
        #            time_constraint_start=parsed_start_time,
        #            time_constraint_end=parsed_end_time,
        #            order_by_names=order,
        #            limit=limit,
        #        )
        # -------------------------------------------------
        

        # -------------------------------------------------
        # Execute MetricFlow query
        # -------------------------------------------------

        result = metricflow_engine.query(request)

        # -------------------------------------------------
        # Convert MetricFlow result to list[dict]
        # -------------------------------------------------

        table = result.result_df

        if table is None:
            return success_response([])

        df = pd.DataFrame(
            table.rows,
            columns=table.column_names,
        )

        data = df.to_dict(orient="records")

        return success_response(data)

    # -----------------------------------------------------
    # Our validation errors
    # -----------------------------------------------------

    except QueryValidationError as error:
        return validation_error_response(error)

    # -----------------------------------------------------
    # MetricFlow / database / runtime errors
    # -----------------------------------------------------

    except Exception as error:
        return metricflow_error_response(error)

# =========================================================
# MCP Tools
# =========================================================


@mcp.tool(
    description="""
    Return all metrics currently available in the dbt Semantic Layer.

    Use this tool to determine the exact metric name before calling
    run_metric_query.

    Do not invent metric names.
    """
)
def get_metrics() -> list[str]:
    return get_metricflow_metrics()



@mcp.tool(
    description="""
    Return all dimensions available for a specific metric.

    The metric must be an exact metric name returned by get_metrics.

    Use this tool before calling run_metric_query to determine which
    dimensions can be used for grouping and filtering.    

    Do not invent dimension names.
    """
)
def get_dimensions(metric: str) -> list[str]:
    return get_metricflow_dimensions([metric])


@mcp.tool(
    description="""
    Return all valid values for the account__state_code dimension.

    Use this tool before filtering a metric query by state.

    The value sent to run_metric_query must exactly match one of the
    values returned by this tool.
    """
)
def get_state_codes() -> list[str]:

    return get_valid_state_codes()


@mcp.tool(
    description="""
    Return all valid values for the account__country dimension.

    Use this tool before filtering a metric query by country.

    The value sent to run_metric_query must exactly match one of the
    values returned by this tool.
    """
)
def get_countries() -> list[str]:

    return get_valid_countries()


@mcp.tool(
    description="""
    Execute a query against the dbt Semantic Layer using MetricFlow.

    Before calling this tool:

    - Use get_metrics to obtain exact metric names.
    - Use get_dimensions to obtain dimensions (group_by) valid for the requested metrics.
    - Use get_state_codes before filtering by account__state_code.
    - Use get_countries before filtering by account__country.

    Do not invent metric names, dimension names, or controlled dimension values.

    The where parameter must contain a valid MetricFlow filter expression.
    Metric and dimension names, dimension values, value types, time range,
    ordering, and limit are validated before MetricFlow is executed.

    start_time and end_time must use ISO format:
    - YYYY-MM-DD
    - or YYYY-MM-DDTHH:MM:SS

    Examples:
    - 2026-06-01
    - 2026-06-01T00:00:00

    Do not use natural-language dates such as
    'June 1, 2026', 'last month', or 'yesterday'.

    Do not generate SQL. Queries are executed only through MetricFlow.

    On success this tool returns:
        {
            "success": true,
            "data": [...],
            "error": null
        }

    On validation or MetricFlow execution failure this tool returns:
        {
            "success": false,
            "data": null,
            "error": {...}
        }
    """
)
def run_metricflow_query(
    metrics: list[str],
    group_by: list[str] | None = None,
    where: str | None = None,
    start_time: str | None = None,
    end_time: str | None = None,
    order: list[str] | None = None,
    limit: int | None = None,
) -> dict[str, Any]:

    return metricflow_query(
        metrics=metrics,
        group_by=group_by,
        where=where,
        start_time=start_time,
        end_time=end_time,
        order=order,
        limit=limit,
    )

@mcp.tool(
    description="""
    Find an Account / Organization and return structured account context
    for explanation, analysis, or knowledge-graph construction.

    Parameters:
    - account_name: required partial or exact account name.
    - state_code: optional state code used to narrow matches.
      Use get_state_codes to obtain valid state-code values.
    - district_name: optional partial or exact district name, primarily used to
      distinguish schools with similar or identical names.

    Account names are not unique.

    If multiple accounts match:
    - Do not arbitrarily select one.
    - Present the matching account names, states, and districts to the user.
    - Ask the user to clarify the state first when possible.
    - If multiple schools still match within the state, ask for the district.
    - Call this tool again with the clarified state_code and/or district_name.

    If exactly one account matches, use the returned structured data to
    explain the account or build an account knowledge graph.

    Important warehouse conventions:
    - 'Unknown' means the source value is missing or unavailable.
    - '1900-01-01' means the date value is missing or unavailable.
    These are placeholder/default values and must not be interpreted as
    actual business values or actual dates.

    Do not invent missing Account attributes or relationships.
    """
)
def get_account(
    account_name: str,
    state_code: str | None = None,
    district_name: str | None = None,
) -> dict[str, Any]:

    return account_query(
        account_name=account_name,
        state_code=state_code,
        district_name=district_name,
    )

# =========================================================
# Server
# =========================================================

if __name__ == "__main__":
    mcp.run(transport="stdio")

pip install dbt-core==1.12.5 dbt-redshift
pip install dbt-metricflow

dbt-core==1.12.5 requires at least one model with day granularity even when not used

There is an existing MetricFlow bug with essentially the same behavior: dbt works, but mf calls dbt's profile loader and reports Could not find profile named .... The issue remains open.

MetricFlow added explicit support for DBT_PROFILES_DIR, so the practical workaround is to tell mf exactly where the profile directory is.
setx DBT_PROFILES_DIR "C:\Users\KDrogaieva\.dbt"

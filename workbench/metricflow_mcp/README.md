pip install fastmcp dbt-metricflow dbt-redshift python-dotenv pandas

pip install pytest

pytest test_metricflow_query.py -v

pip install sqlalchemy sqlalchemy-redshift psycopg2-binary


metric_time__fiscalmonth, metric_time__fiscalyear,metric_time__mon_year are valid custom metrc_time dimensions 
but they are not returned as a separate dimension  in mf list dimensions --metrics arr
they need to be added manually in the function which returns list of valid dimensions
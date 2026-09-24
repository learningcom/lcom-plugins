{{ config(materialized='view', bind=False) }}

select
mon_year, 
mon_firstday, 
mon_lastday, 
fiscalyear,
fiscalyear_mon, 
fiscalyear_startdate, 
fiscalyear_enddate, 
schoolyear, 
schoolyear_mon, 
schoolyear_startdate, 
schoolyear_enddate
from {{ source('common', 'dim_month') }}

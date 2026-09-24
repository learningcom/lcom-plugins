{{ config(materialized='view', bind=False) }}
 
with 
data as (
select
mon_year, 
mon_lastday, 
organization_school_id as account_id, 
school_cnt_students as active_users, 
school_students_launches as launches,
school_cnt_students_month as active_users_month, 
school_students_launches_month as launches_month
from {{ source('content_delivery_usage', 'fact_students_usage_monthly_snapshots') }}
where topic='(All)'
and product_category='(All)'
and grade_level='(All)'
)
select *
from data

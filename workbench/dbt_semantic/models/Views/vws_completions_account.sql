{{ config(materialized='view', bind=False) }}
 
with 
data as (
select
mon_year, 
mon_lastday, 
organization_school_id as account_id, 
school_cnt_student_completions as users_with_completions, 
school_cnt_completions as completions,
school_cnt_student_completions_month as users_with_completions_month, 
school_cnt_completions_month as completions_month
from {{ source('content_delivery_usage', 'fact_students_completions_monthly_snapshots') }}
where topic='(All)'
and product_category='(All)'
and grade_level='(All)'
)
select *
from data

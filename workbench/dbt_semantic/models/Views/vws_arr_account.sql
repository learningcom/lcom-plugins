{{ config(materialized='view', bind=False) }}

select
    f.mon_year,
    f.mon_lastday,
    f.account_id,
    sum(
        case when f.arr_type = 'Preliminary'
             then f.arr_amount else 0 end
    ) as preliminary_arr,
    sum(
        case when f.arr_type = 'Backdated'
             then f.arr_amount else 0 end
    ) as backdated_arr,
    sum(
        case when f.arr_type = 'True'
             then f.arr_amount else 0 end
    ) as true_arr
from {{ source('revenue', 'vw_fact_arr') }} f
where f.record_type = 'ARR'
group by
    f.mon_year,
    f.mon_lastday,
    f.account_id

{{ config(materialized='view', bind=False) }}
with dim_month as --Thread to calculate monthly metrics
(select c.mon_year, c.mon_lastday
from {{ source('common', 'dim_month') }}  c 
where mon_year between 202207 and to_char(GetDate(),'yyyymm')
)
--
,rawdata as (
select distinct
m.mon_year,
m.mon_lastday,
organization_district_id account_id,
flo.sku_id,
flo.schoolcount,
flo.studentcount
from {{ source('licensing', 'vw_fact_license_order') }} flo
--latest in the month order
join dim_month m
on case when m.mon_lastday<trunc(GETDATE()) then m.mon_lastday else trunc(GETDATE()) end between flo.startdate and flo.expirationdate
--on m.mon_lastday between flo.startdate and flo.expirationdate
join {{ source('common', 'dim_account') }} a
on flo.organization_district_id = a.account_id
where a.lcom_trial=false 
and a.lcom_demo=false
and flo.valid='Y'
and flo.enforcedaterestrictions='y'
)
,data as (
select
mon_year,
mon_lastday,
account_id,
sku_id,
sum(schoolcount) as schoolcount,
sum(studentcount) as studentcount
from rawdata r
group by 
mon_year,
mon_lastday,
account_id,
sku_id
)
select 
mon_year,
mon_lastday,
account_id,
max(schoolcount) as schoolcount,
max(studentcount) as studentcount
from data
group by
mon_year,
mon_lastday,
account_id

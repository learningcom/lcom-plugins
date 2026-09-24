{{ config(materialized='view', bind=False) }}



select
a.account_id,
--
--
a.sfdc_account_id,
a.sfdc_name,
a.sfdc_parent_id,
a.sfdc_parent_name,
a.sfdc_ultimate_parent_id,
a.sfdc_ultimate_parent_account,
a.conformed_district_id,
a.conformed_district_sfdc_account_id,
a.conformed_customer_id,
a.conformed_customer_sfdc_account_id,
--
a.name,
a.district_name,
a.customer_name ,
case when a.conformed_customer_id=a.conformed_district_id then '(Districts)' else a.customer_name end as display_customer_name,
a.country,
a.state_code ,
a.state_name,
a.county,
a.state_initiative,
a.sfdc_state_program_eligible,
a.lcom_trial,
a.lcom_demo,
a.lcom_organization_id,
a.lcom_organization_name,
a.lcom_organization_type,
a.lcom_parent_organization_id,
a.lcom_parent_organization_name,
a.lcom_nces_id,
a.lcom_external_sis_id,
a.sfdc_owner_id as owner_id,
a.owner,
a.enrollment,
a.urban_rural,
a.account_type,
a.customer_level,
--
la.has_product_licenses,
la.has_product_usage,
la.total_won_opportunities, 
la.total_open_opportunities, 
la.total_won_deals,
la.total_won_state_program_deals,
la.latest_start_date, 
la.latest_end_date, 
la.latest_open_opportunities_modified_date, 
la.first_invoiced_date, 
la.total_training_sessions, 
la.latest_training_session_on, 
la.total_cases, 
la.currently_open_cases, 
la.latest_case_created_date, 
la.latest_open_case_modified_date
--
from {{ source('common', 'dim_account') }}  a
join {{ source('reporting', 'dim_account_metrics') }} la
on la.account_id = a.account_id



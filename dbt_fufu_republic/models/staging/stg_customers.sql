-- models/staging/stg_customers.sql

with source as (
    select * from {{ source('fufu_republic', 'customers') }}
)

select
    customer_id as id,             -- Renaming for consistency
    first_name as first_name,
    last_name as last_name,
    email as email,
    created_at::timestamp as created_at  -- Casting to timestamp if necessary
from source

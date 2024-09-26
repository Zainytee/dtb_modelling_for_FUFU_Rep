-- models/staging/stg_branches.sql

with source as (
    select * from {{ source('fufu_republic', 'branches') }}
)

select
    branch_id as id,                -- Renaming for consistency
    branch_name as name,
    branch_location as location,
    city as city,
    region as region,
    created_at::timestamp as created_at
from source

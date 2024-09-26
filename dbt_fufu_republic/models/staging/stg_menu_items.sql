-- models/staging/stg_menu_items.sql

with source as (
    select * from {{ source('fufu_republic', 'menu_items') }}
)

select
    menu_item_id as id,            -- Renaming for consistency
    item_name as name,
    price::decimal(10, 2) as price,  -- Casting to decimal for price
    created_at::timestamp as created_at
from source

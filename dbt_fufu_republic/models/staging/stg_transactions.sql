-- models/staging/stg_transactions.sql

with source_data as (
    select
        transaction_id,  
        customer_id,  
        branch_id, 
        menu_item_id,  
        cast(transaction_date as date) as transaction_date,  
        cast(total_amount as decimal(10, 2)) as total_amount,  
        quantity
    from {{ source('fufu_republic', 'transactions') }}  -- Reference to your source
)

select
    transaction_id,
    customer_id,
    branch_id,
    menu_item_id,
    transaction_date,
    total_amount,
    quantity
from source_data

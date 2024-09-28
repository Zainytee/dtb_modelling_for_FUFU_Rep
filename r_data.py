# Importing necessary libraries
import os
import pandas as pd
import random
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Creating function for the random selection in the synthetic data
def random_gender():
    return random.choice(['Male', 'Female'])

def random_loyalty_status():
    return random.choice(['Bronze', 'Silver', 'Gold', 'Platinum', 'None'])

def random_item_category():
    return random.choice(['Appetizer', 'Main Course', 'Dessert', 'Beverage'])

def random_region():
    return random.choice(['South_East', 'South_West', 'South_South','North_Centra','North_East', 'North_West'])

def random_city():
    return random.choice(["Lagos", "Abuja", "Port Harcourt", "Ibadan", 'UYO', 'KANO'])

def random_name():
    nigerian_food_items = [
        'Jollof Rice', 'Pounded Yam', 'Egusi Soup', 'Fufu', 
        'Efo Riro', 'Fried Rice', 'Beans and Plantain', 'Suya',
        'Moi Moi', 'Pepper Soup', 'Akara', 'Ogbono Soup', 'Amala',
        'Boli', 'Chicken Stew', 'Goat Meat Peppersoup', 'Ewa Agoyin', 
        'Juice', 'Wine'
    ]
    return random.choice(nigerian_food_items)


def random_food_description():
    descriptions = [
        "Deliciously spicy", "Freshly prepared", "Crispy and savory",
        "Succulent and juicy", "A delightful blend of flavors",
        "Richly flavored", "Homemade with love", "Authentic taste",
        "Perfectly cooked", "Mouthwatering delight"
    ]
    return random.choice(descriptions)

# Generate synthetic customer data
def generate_customers(num_records):
    customers = []
    for _ in range(num_records):
        customer = {
            'customer_id': fake.uuid4(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'address': fake.address(),
            'gender': random_gender(),
            'loyalty_status': random_loyalty_status()
        }
        customers.append(customer)
    return pd.DataFrame(customers)

# Generate synthetic menu data without duplicates
def generate_menu_items(num_records):
    menu_items = []
    for _ in range(num_records):
        menu_item = {
            'item_id': fake.uuid4(),
            'name': random_name(),
            'price': round(random.uniform(3000, 10000), 2),
            'item_category': random_item_category(),
            'food_description': random_food_description()
        }
        menu_items.append(menu_item)
    return pd.DataFrame(menu_items)

# Generate synthetic branch data
def generate_branches(num_records):
    branches = []
    while len(branches) < num_records:
        branch = {
            'branch_id': fake.uuid4(),
            'branch_name': fake.city(),
            'branch_location': fake.address().replace("\n", ", "),
            'city': random_city(),
            'region': random_region()
        }
        branches.append(branch)
    return pd.DataFrame(branches)

# Generate synthetic transaction data
def generate_transactions(num_records, customers, menu_items, branches):
    transactions = []
    for _ in range(num_records):
        transaction = {
            'transaction_id': fake.uuid4(),
            'customer_id': random.choice(customers['customer_id']),
            'branch_id': random.choice(branches['branch_id']),
            'item_id': random.choice(menu_items['item_id']),
            'amount': round(random.uniform(3000, 50000), 2),
            'payment_method': random.choice(['Cash', 'Debit Card', 'Online']),
            'transaction_date': fake.date_this_year(),
            'dining_option': random.choice(['Dine-in', 'Take-out', 'Online']),
        }
        transactions.append(transaction)
    return pd.DataFrame(transactions)

# Generate and save the data
num_records = 1000

customers_df = generate_customers(num_records)
menu_items_df = generate_menu_items(50)
branches_df = generate_branches(10)
transactions_df = generate_transactions(num_records, customers_df, menu_items_df, branches_df)

# Save the data to CSV files
customers_df.to_csv('customers.csv', index=False)
menu_items_df.to_csv('menu_items.csv', index=False)
branches_df.to_csv('branches.csv', index=False)
transactions_df.to_csv('transactions.csv', index=False)

print("Synthetic data generated and saved as CSV files!")

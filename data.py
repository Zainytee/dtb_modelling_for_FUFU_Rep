#Importing necessary libraries
import os
from faker import Faker
import pandas as pd
import random

#Initializing Faker instance
fake = Faker()

#setting seed for Faker
Faker.seed(3007)

import pandas as pd
from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

#Creating function for the random selection in the synthetic data
def random_gender():
    return random.choice(['Male', 'Female', 'Other'])

def random_loyalty_status():
    return random.choice(['Bronze', 'Silver', 'Gold', 'Platinum', 'None'])

def random_item_category():
    return random.choice(['Appetizer', 'Main Course', 'Dessert', 'Beverage'])

def random_food_description():
    return fake.sentence(nb_words=10)  # Generate a random food description

def random_region():
    return random.choice(['South_East', 'South_West', 'South_South','North_Centra','North_East', 'North_West'])


# Define a custom list of Nigerian food items with descriptions
nigerian_food_items_with_desc = {
    'Jollof Rice': 'A spicy and flavorful rice dish made with tomatoes, onions, and a mix of spices.',
    'Pounded Yam': 'A smooth, dough-like side dish served with soups like Egusi or Ogbono.',
    'Egusi Soup': 'A rich, thick soup made from melon seeds and typically served with fufu or pounded yam.',
    'Fufu': 'A dough-like meal made from cassava, yams, or plantains, usually served with a variety of soups.',
    'Efo Riro': 'A traditional Yoruba stew made with leafy vegetables, meat, and spices.',
    'Fried Rice': 'Rice stir-fried with vegetables and proteins, seasoned with herbs and spices.',
    'Beans and Plantain': 'Boiled beans served with fried or roasted plantains.',
    'Suya': 'Spicy grilled skewers of meat, often served with onions and tomatoes.',
    'Moi Moi': 'A steamed bean pudding made from blended beans and spices.',
    'Pepper Soup': 'A spicy broth usually made with fish, goat meat, or chicken, perfect for a cold day.',
    'Akara': 'Deep-fried bean cakes, crispy on the outside and soft inside.',
    'Ogbono Soup': 'A savory soup made from ground Ogbono seeds, often served with fufu or pounded yam.',
    'Amala': 'A starchy side dish made from yam flour, typically served with a soup like Ewedu or Gbegiri.',
    'Boli': 'Roasted plantain, often served with groundnut or spicy sauce.',
    'Chicken Stew': 'A tomato-based stew cooked with tender chicken and spices.',
    'Goat Meat Peppersoup': 'A spicy, aromatic soup with chunks of tender goat meat.',
    'Ewa Agoyin': 'A mashed bean dish served with spicy, flavorful pepper sauce.',
    #Beverages
    'Zobo': 'A refreshing hibiscus drink made from dried roselle leaves, sweetened and served cold.',
    'Chapman': 'A fruity cocktail made with a blend of sodas, grenadine, and fresh citrus slices.',
    'Kunu': 'A traditional drink made from grains like millet or sorghum, with a slightly spicy and sweet flavor.',
    'Juice': 'Freshly Squeezed fruit juice.',
    'Fura da Nono': 'A nutritious drink made from fermented milk and millet.',
    'Malt Drink': 'A non-alcoholic, sweet malted drink that is a popular soft drink option.',
    'Bottled Water': 'Pure, refreshing bottled water.',
    'Soft Drinks': 'Carbonated drinks available in various flavors, served cold.'
}

def random_food_description():
    item, description = random.choice(list(nigerian_food_items_with_desc.items()))
    return item, description

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
    

# Generate synthetic menu data
def generate_menu_items(num_records):
    menu_items = []
    for _ in range(num_records):
        item_name, item_description = random_food_description()
        menu_item = {
            'item_id': fake.uuid4(),
            'name': item_name,
            'price': round(random.uniform(3000, 10000), 2),  # Price between 3000 and 10000
            'item_category': random_item_category(),
            'food_description' : item_description
        }
        menu_items.append(menu_item)
    return pd.DataFrame(menu_items)

# Generate synthetic branch data
def generate_branches(num_records):
    branches = []
    for _ in range(num_records):
        branch = {
            'branch_id': fake.uuid4(),
            'branch_name': fake.city(),
            'branch_location': fake.address().replace("\n", ", "),
            'city': fake.city(),
            'state': fake.state(),
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
menu_items_df = generate_menu_items()
branches_df = generate_branches(10)
transactions_df = generate_transactions(num_records, customers_df, menu_items_df, branches_df)



# Define base directory
base_dir = 'C:/Users/zaina/Documents/Core_Data_Engineering/DBT_MODELLING/dtb_modelling_for_FUFU_Rep/'

# Save the data to CSV files (to be used as seed data in dbt)
customers_df.to_csv(os.path.join(base_dir, 'customers.csv'), index=False)
menu_items_df.to_csv(os.path.join(base_dir, 'menu_items.csv'), index=False)
branches_df.to_csv(os.path.join(base_dir, 'branches.csv'), index=False)
transactions_df.to_csv(os.path.join(base_dir, 'transactions.csv'), index=False)


print("Synthetic data generated and saved as CSV files!")






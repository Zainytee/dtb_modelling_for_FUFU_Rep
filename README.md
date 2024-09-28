# dtb_modelling_for_FUFU_Rep

Welcome to the **dbt_modelling_for_fufu_Rep** project! This repository is a part of my journey in data engineering, focusing on building a robust data pipeline for Fufu Republic, a popular restaurant chain in Nigeria. The aim is to harness the power of data for informed decision-making and improved customer experiences.

## Project Overview

In this project, I've implemented a series of transformations and models using **dbt** (data build tool) to prepare and analyze data from various sources, including branches, customers, menu items, and transactions. By generating synthetic data with Python's `Faker` library, I've created a realistic dataset that mimics the operations of Fufu Republic.

### Key Components

- **Sources**: Raw data tables that serve as the foundation for our models.
- **Staging Models**: Light transformations mapping 1:1 with source tables, ensuring consistency and preparing data for further analysis.
- **Data Quality Tests**: Implemented tests to ensure data integrity and reliability throughout the pipeline.
- **Synthetic Data Generation**: Used the `Faker` library to generate sample data for branches, customers, menu items, and transactions.

## Generating Synthetic Data with Faker

To simulate real-world data, I used the `Faker` Python library to generate synthetic data for the database tables. Here’s how you can generate the same dataset:

### Step 1: Install Faker

First, install the `Faker` library in your Python environment:

```bash
pip install Faker
```

### Step 2: Generate Synthetic Data
Here’s an example of how I used Faker to generate data for the branches, customers, menu_items, and transactions tables:

```python
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

num_records = 100
menu_items_df = generate_menu_items(num_records)
menu_items_df.to_csv('menu_items.csv', index=False)
```

Similar process for repeated for customers, branches, and transactions. This data is then used as the seed for the dbt transformations.

### Getting Started

To get started with the project, follow these steps:

### STEP 1: Clone the Repository: 

```bash
git clone https://github.com/Zainytee/dbt_modelling_for_fufu_Rep.git
```

### STEP 2: Install Dependencies: 

Ensure dbt is installed in your environmnet  along with your chosen data warehouse.

```bash
cd dbt_fufu_republic
pip install dbt-snowflake

```

### STEP 3: Set Up Your Environment: 

Configure your profiles.yml file to connect to your Snowflake database.

### STEP 4: Prepare your seed files:

Make sure the CSV files with the seed data are inside the data folder in your dbt project structure (e.g., models/seeds or data folder).

### STEP 5: Run dbt seed::

Execute the following command to push the data to Snowflake:

```bash
dbt seed
```
This command will read the CSV files from the data directory and upload them to Snowflake as tables in your database. The data will be loaded based on how your dbt_project.yml and the seed configuration are set up.

### STEP 6: Run the Models:

Navigate to the project directory and run the dbt models:

```bash
dbt run
```
### STEP 7: Test the Models:

After running the models, ensure everything works as expected by executing:

```bash
dbt test
```
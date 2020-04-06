import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')

#we now analyze a sub-dataframe of products sold at stten island
print(inventory.head(10))
staten_island = inventory.head(10)
product_request = staten_island.product_description

#select rows to find out what seeds are sold in brooklyn
seed_request = inventory.loc[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)

#investigating the inventory
inventory['in_stock'] = inventory.apply(lambda row: 'True' if row['quantity'] > 0 else 'False', axis = 1)
inventory['total_value'] = inventory.apply(lambda row: row['price'] * row['quantity'], axis=1)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description']=inventory.apply(combine_lambda, axis=1)
print(inventory)

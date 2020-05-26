import pandas as pd 
from matplotlib import pyplot as plt 

#load and inspect data
restaurants=pd.read_csv('restaurants.csv')
print(restaurants.head(10))
#count no of cuisines offered
cuisine_options_count = restaurants.cuisine.nunique()
print(cuisine_options_count)
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(cuisine_counts)

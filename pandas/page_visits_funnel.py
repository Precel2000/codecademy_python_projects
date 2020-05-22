import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#combine visits and cart, inspect length
visits_cart = pd.merge(visits, cart, how='left')
print(len(visits_cart))

cart_time_null = len(visits_cart) - visits_cart.cart_time.count()
#alternatively, visits_cart[visit_cart.cart_time.isnull()] selects all rows with the null value
no_cart_per = 100 * float(cart_time_null)/len(visits_cart)
print("didnt add to cart [%]:")
print(no_cart_per)
cart_checkout = cart.merge(checkout, how='left')
checkout_null = len(cart_checkout) - cart_checkout.checkout_time.count()
no_checkout_per = 100 * float(checkout_null)/len(cart_checkout)
print("null checkout values [%]:")
print(no_checkout_per)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

purchase_null = len(all_data) - all_data.purchase_time.count()
no_purchase_per = 100 * float(purchase_null)/len(all_data)
print("did not purchase [%]:")
print(no_purchase_per)

#the weakest step of the chain is adding a t-shirt to the cart. This is normal behaviour, but it can be altered by offering a time-sensitive offer upon the user visiting a website
print(all_data.head())
#create new column
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase)
#calculate the average time it takes to purchase product
print(all_data.time_to_purchase.mean())

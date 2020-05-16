
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#calculate average haircut price
total_price = 0
for price in prices:
  total_price+= price
av_price = total_price/len(prices)
print("Average Haircut Price: " + str(av_price))

#create new list of prices, reduced by 5
new_prices=[pr-5 for pr in prices]
print(new_prices)

#calculate revenue
total_revenue=0
for i in range(len(hairstyles)):
  total_revenue+= prices[i]*last_week[i]
print("Total Revenue: " + str(total_revenue))
print("Average Daily Revenue is: " + str(total_revenue/7))

#identify cuts that cost less than 30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]
print("Cuts under 30: "+ str(cuts_under_30))

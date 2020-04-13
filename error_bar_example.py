import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
plt.bar(range(len(drinks)), ounces_of_milk, color='navy', yerr=error, capsize=5)
plt.xlabel('drink')
plt.ylabel('ounces of milk used')
plt.title('milk contained in drinks')
plt.show()

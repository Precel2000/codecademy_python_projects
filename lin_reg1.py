from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

#create lin reg model
line_fitter = LinearRegression()
line_fitter.fit(temperature, sales)
#list of predicted sales values
sales_predict = line_fitter.predict(temperature)

#plot the source data
plt.plot(temperature, sales, 'o')
plt.plot(temperature, sales_predict, color='purple')
plt.show()

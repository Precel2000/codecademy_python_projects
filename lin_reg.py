import pandas as pd
import matplotlib.pyplot as plt

#load data
df = pd.read_csv("heights.csv")
X = df["height"]
y = df["weight"]

#auxilliary function to get gradient at specified b
def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

#auxilliary function to get gradient at specified m
def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Function to calculate the step_gradient
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
#gradient_descent function to altern b and m  
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return [b,m]  

#call the gradient_descent function
b,m = gradient_descent(X,y,0.0001,1000)
#create a list of predicted y-values using list comprehension
y_predictions= [x*m+b for x in X]
#plot the source data 
plt.plot(X, y, 'o')
#plot predicted line
plt.plot(X, y_predictions, 'o')
plt.show()

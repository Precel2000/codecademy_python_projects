import pandas as pd
import numpy as np
from weather_data import london_data

print(london_data.head())

#finding the mean and std for the temperature in each month
for i in range(1, 13):
  #select temperature data for the given month
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  #find the mean of the dataset
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  #find the standard deviation of the dataset
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
  
#investigating the daily amount of rain in each month
for i in range(1, 13):
  #select precipitation data for the given month
  month = london_data.loc[london_data["month"] == i]  ["dailyrainMM"]
  #find the mean of the dataset
  print("The mean of daily rain in month "+str(i) +" is "+ str(np.mean(month)))
  #find the standard deviation of the dataset
  print("The standard deviation of daily rain in month "+str(i) +" is "+ str(np.std(month)) +"\n")

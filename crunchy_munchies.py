import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')

average_calories = np.mean(calorie_stats)
print("average calories: ")
print(average_calories)
print(" ")
calorie_stats_sorted = np.sort(calorie_stats)
print("sorted list of calories: ")
print(calorie_stats_sorted)
print(" ")
median_calories=np.median(calorie_stats)
print("median is: " + str(median_calories))

nth_percentile = np.percentile(calorie_stats, 4)
#print(nth_percentile)
more_calories = np.mean(calorie_stats > 60)*100
print(str(more_calories) + "% of our cometitors have more calories than our cereal")

calorie_std = np.std(calorie_stats)
print("the sd is: " + str(calorie_std))
print("CrunchieMunchies is the cereal of choice if u value your body. With only 60cal per serving - less than " + str(more_calories) + " of cereals on the market do")

import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# we create the first figure
plt.figure(figsize=(12,8))
ax1 = plt.subplot(1,2,1)
#create list of x-values
x_values = range(len(months))
#plot graph of visits_per_month against months
plt.plot(x_values, visits_per_month, color='purple', marker="s")
#label the ticks
ax1.set_xticklabels(months)
#label the axes
ax1.set(xlabel='month', ylabel='page visits')
#ensure appropriate number of ticks
ax1.set_xticks(x_values)
plt.title('page visits in each month')

#we create the second figure
ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month, color='green')
plt.plot(x_values, persian_limes_per_month, color='navy')
plt.plot(x_values, blood_limes_per_month, color='red')
#create legend, adjust ticks, add axis labels and title to enhance readability 
ax2.legend(['key', 'persian', 'blood'])
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.xlabel('months')
plt.ylabel('limes sold')
ax2.set(title='key, persian, and blood limes sold per month')
plt.show()
plt.savefig('subline_limes.png')

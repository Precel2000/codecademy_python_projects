import codecademylib
from matplotlib import pyplot as plt
import numpy as np

#save data to lists
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

#create lists of bottoms for chart components
c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

#create the figure
plt.figure(figsize=(10,8))
#create the stached bar chart components
plt.bar(range(len(unit_topics)), As)
plt.bar(range(len(unit_topics)), Bs, bottom=As)
plt.bar(range(len(unit_topics)), Cs, bottom=c_bottom)
plt.bar(range(len(unit_topics)), Ds, bottom=d_bottom)
plt.bar(range(len(unit_topics)), Fs, bottom=f_bottom)

#create set of axes
ax=plt.subplot()

#customize the graph
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
ax.set_title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')

plt.show()

#save work
plt.savefig('my_stacked_bar.png')

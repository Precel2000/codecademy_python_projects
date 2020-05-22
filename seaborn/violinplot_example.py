import codecademylib3_seaborn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid") # options include: darkgrid, whitegrid, dark, white, and ticks
sns.set_palette("pastel") # other options include: paired (?),deep, muted, pastel, bright, dark, and colorblind (!) 
                          # u can also specify how many colors we want like this: sns.color_palette("Paired", 9)
                          # and view them like this: sns.palplot(custom_palette)

#the scale can be controlled by passing paper, notebook, talk, or poster to sns.set_context
sns.set_context("talk", rc={'axes.labelsize': 17.6,
 'axes.titlesize': 19.200000000000003,
 'font.size': 19.200000000000003,
 'grid.linewidth': 0.8,
 'legend.fontsize': 15.0,
 'lines.linewidth': 2.8000000000000003,
 'lines.markeredgewidth': 0.0,
 'lines.markersize': 11.200000000000001,
 'patch.linewidth': 0.48,
 'xtick.labelsize': 16.0,
 'xtick.major.pad': 11.200000000000001,
 'xtick.major.width': 1.6,
 'xtick.minor.width': 0.8,
 'ytick.labelsize': 16.0,
 'ytick.major.pad': 11.200000000000001,
 'ytick.major.width': 1.6,
 'ytick.minor.width': 0.8})

#plot the graph
sns.violinplot(data=df, x='label', y='value')

#despines the top, left and right side of the chart 
#it will cut the axes to fit the ticks present. 
#the spine is moved away from the data
sns.despine(left=True, offset=10, trim=True))

#sinplot() can be used in place of plt.show()
plt.show()

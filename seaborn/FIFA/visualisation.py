import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')

#add column called 'Total Goals'
df['Total Goals'] = df['Home Team Goals']+df['Away Team Goals']
#styling
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.25)
#create figure and axes for the plot with the specified size
f, ax = plt.subplots(figsize=(20,7))
#create the barplot
ax = sns.barplot(data=df, x='Year', y='Total Goals')
ax.set_title("Average FIFA World Cup Goals Per Match By Year")
plt.show()

#load dataframe for second visialisation
df_goals=pd.read_csv('goals.csv')
#create the figure for the second graph
f, ax2 = plt.subplots(figsize=(12,7))
#specify styling
sns.set_palette("Spectral")
#plot graph
ax2 = sns.boxplot(data=df_goals, x='year', y='goals')
ax2.set_title("Box plot illustrating average goals per match in a year")
plt.show()

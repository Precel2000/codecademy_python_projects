import codecademylib
import pandas as pd

#load and view data
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

#inspect how views are distributed amongst sources
views_per_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click']= ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])

#inspect whether ad A or B is more effective

#check if the sample size for A and B are equal
group_AB = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(group_AB)

#we count the number of times ad A and B have been clicked on, repectively
superior_ad = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
#we pivot the table so that it is easier to read
superior_pivot = superior_ad.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()
#how successful each ad type was (more success = higher % of ppl who saw the ad clicked on it)
superior_pivot['percent_clicked'] = 100 * superior_pivot[True]/(superior_pivot[True]+superior_pivot[False])
print(superior_pivot)

#create seperate dataframes for ad A and B
a_clicks = ad_clicks.loc[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks.loc[ad_clicks['experimental_group'] == 'B']
print(a_clicks)
print(b_clicks)

#investigate how the distribution changed by date for group A
a_per_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
a_pivot = a_per_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
a_pivot['percentage']=100*a_pivot[True]/(a_pivot[True]+a_pivot[False])
print(a_pivot)

#do the same for group B
b_per_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_pivot = b_per_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
b_pivot['percentage']=100*b_pivot[True]/(b_pivot[True]+b_pivot[False])
print(b_pivot)

#conclusion:ad A is more effective, I would recommand that the company shows ad A in favour of ad B

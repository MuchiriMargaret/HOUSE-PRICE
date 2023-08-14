# importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Acquiring dataset from files
df = pd.read_csv("House_price_dataset.csv")
chunk= df.head(30000)
# print(chunk)
# displaying first few rows to check the data
print(chunk.head())

# Description of columns in this dataset
# print(chunk.describe())

# information on the data
# print(chunk.info())
# print(chunk.columns)

# Drop unnecessary columns
columns_to_drop= ['property_id','location_id','page_url','latitude',
                 'longitude','Area Type']
new_df=chunk.drop(columns_to_drop, axis='columns')
# print(new_df)
# print(new_df.columns)

# unique elements in the dataset
unique=new_df.nunique
# print(unique)

# find null values
null_values=new_df.isnull().sum()
# print(null_values)

# EDA
totalValues=new_df.index.stop
# print(totalValues)
null_values=new_df['agency'].isnull().sum()
# print(null_values)

# same as that of agent
percentage=null_values/totalValues*100
# print(percentage)

# unique values of agency and agent
uniqueAgency=new_df['agency'].unique()[0:]
list=uniqueAgency
# print(list)
# print(new_df['agent'].unique()[0:])
# retrieving last row
lastRow=new_df.iloc[29999]
# print(lastRow)

# fill null values
agency_filled=new_df['agency'].fillna('Self',inplace=True)
# print(agency_filled)
agent_filled=new_df['agent'].fillna('Self',inplace=True)
# print(agent_filled)
# print(new_df.isnull().sum())

# find duplicated values
v=new_df.duplicated(subset=['agency','agent'], keep=False)
# print(v)
# most duplicated values in columns
frequent_values=new_df.mode(axis='index',numeric_only=False,dropna=True)
# print(frequent_values)
sum_duplicate=new_df.duplicated().sum()
print(sum_duplicate)
# delete duplicates
print(new_df.drop_duplicates(inplace=True))
print(new_df.duplicated().sum())

# value occurences
property=new_df['property_type'].value_counts(ascending=False)
# print(property)
loc=new_df['location'].value_counts(ascending=False)
# print(loc)
city=new_df['city'].value_counts(ascending=False)
# print(city)
purpose=new_df['purpose'].value_counts(ascending=False)
# print(purpose)
agency=new_df['agency'].value_counts(ascending=False)
# print(agency)
agent=new_df['agent'].value_counts(ascending=False)
# print(agent)
area_cat=new_df['Area Category'].value_counts(ascending=False)
# print(area_cat)

# number of property types in each city
print(new_df.groupby('city')['property_type'].value_counts())

# # VISUALIZE THE RESULTS
# tab=new_df.pivot_table(index='property_type',columns='city',
#                        aggfunc='size',fill_value=0)
# cities = new_df['city'].tolist()
# colors= ['purple','brown','green','red','blue','black','yellow']

# #  subplots for each city
# fig, axes = plt.subplots(nrows=1, ncols=len(cities),figsize=(14,6))
# # create a bar plot
# for i, city in enumerate(cities):
#     ax = axes[i]if len(cities) > 1 else axes
#     tab[city].plot(kind='bar', color=colors, ax=ax)
#     ax.set_title(city)
#     ax.set_xlabel('property Type')
#     ax.set_ylabel('count')
#     for p in ax.patches:
#         ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2.,
#                                            p.get_height()), ha='center', va='center')
# # spacing subplot
# # plt.tight_layout()        
# plt.show()
cities = new_df['city'].tolist()
print
property_type = new_df['property_type'].tolist()
data = np.random.rand(len(property_type), len(cities))
fig, ax = plt.subplots()
heatmap = ax.imshow(data, cmap='coolwarm')

ax.set_xticks(np.arange(len(cities)))
ax.set_xticks(np.arange(len(property_type)))
ax.set_xticklabels(cities)
ax.set_yticklabels(property_type)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
cbar = ax.figure.colorbar(heatmap,ax=ax)
cbar.ax.set_ylabel('Value')

ax.set_title('Property Distribution')
plt.show()

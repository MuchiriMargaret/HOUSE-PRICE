import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("House_Price_dataset.csv")
print(df.head())
# occurrence=new_df.apply(pd.Series.value_counts(dropna=True))
# print(occurrence)

# all_columns=['proprerty_type','location','city','area','purpose',
            #  'bedrooms','agency','agent','Area Category']
# for column in all_columns:
    # calc = new_df.mode(column)
    # print (calc)
# count=new_df.groupby(['property_type','location','city']).size()
# print(count)
Data={
    'city': ['Faisalabad', 'Faisalabad', 'Faisalabad', 'Faisalabad', 'Faisalabad', 'Faisalabad', 'Islamabad', 'Islamabad', 'Islamabad', 'Islamabad', 'Islamabad', 'Islamabad', 'Islamabad', 'Karachi', 'Karachi', 'Karachi', 'Karachi', 'Karachi', 'Karachi', 'Karachi', 'Karachi', 'Lahore', 'Lahore', 'Lahore', 'Lahore', 'Lahore', 'Lahore', 'Lahore', 'Rawalpindi', 'Rawalpindi', 'Rawalpindi', 'Rawalpindi', 'Rawalpindi', 'Rawalpindi', 'Rawalpindi'],
    'property_type': ['House', 'Upper Portion', 'Lower Portion', 'Room', 'Flat', 'Farm House', 'House', 'Flat', 'Upper Portion', 'Lower Portion', 'Farm House', 'Room', 'Penthouse', 'Flat', 'House', 'Upper Portion', 'Lower Portion', 'Penthouse', 'Farm House', 'Room', 'House', 'Flat', 'House', 'Flat', 'Farm House', 'Upper Portion', 'Lower Portion', 'Room', 'Penthouse', 'House', 'Flat', 'Upper Portion', 'Lower Portion', 'Farm House', 'Room', 'Penthouse']
}
df=pd.DataFrame(Data)
print(df)
# creating bar plots
tab=df.groupby(['city', 'property_type']).size().reset_index(name='count')
pivot_data=tab.pivot(index='property_type', columns='city',values='count').fillna(0)
ax=pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6))
ax.set_xlabel('property_type')
ax.set_ylabel('count')
ax.set_title('city')
plt.xticks(rotation=45)
plt.legend(title='city', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
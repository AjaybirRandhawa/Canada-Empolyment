import matplotlib.pyplot as plt #For data visualization
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv("../input/employment-rate-canada/example_data.csv")
df.head()
dfMale = df.loc[(df['sex'] == 'Males') & (df['variable'] == 'Employment')]
df1 = dfMale.drop(columns=['month', 'variable','sex'])
df1["Total"] = df1.sum(axis=1)
dfMale = dfMale.join(df1["Total"])
dfMale = dfMale.drop(columns=['variable', 'sex'])
dfMale.head()
dfFemale = df.loc[(df['sex'] == 'Females') & (df['variable'] == 'Employment')]
df2 = dfFemale.drop(columns=['month', 'variable','sex'])
df2["Total"] = df2.sum(axis=1)
dfFemale = dfFemale.join(df2["Total"])
dfFemale = dfFemale.drop(columns=['sex', 'variable'])
dfFemale.head()
dfMale['month'] = pd.to_datetime(dfMale['month'].astype(str), format='%Y%')
dfMale.reset_index(drop=True, inplace=True)
dfMale.columns=['Year', 'Alberta','British Columbia','Manitoba','New Burnswick','Newfoundland and Labrador','Nova Scotia','Ontario','PEI','Quebec','Saskatchewan','Total']
dfFemale['month'] = pd.to_datetime(dfFemale['month'].astype(str), format='%Y%')
dfFemale.reset_index(drop=True, inplace=True)
dfFemale.columns=['Year', 'Alberta','British Columbia','Manitoba','New Burnswick','Newfoundland and Labrador','Nova Scotia','Ontario','PEI','Quebec','Saskatchewan','Total']

#Group data by year for Males
grouped = dfMale.groupby(dfMale['Year'].map(lambda x: x.year), as_index=False)

start = dfMale.iloc[0:1]
dfMale = grouped.last()
dfMale = start.append(dfMale)
dfMale.reset_index(drop=True, inplace=True)
dfMale[['TC%']]=dfMale.sort_values(['Year'])[['Total']].pct_change()*100
#Group data by year for Females
grouped = dfFemale.groupby(dfFemale['Year'].map(lambda x: x.year), as_index=False)

start = dfFemale.iloc[0:1]
dfFemale = grouped.last()
dfFemale = start.append(dfFemale)
dfFemale.reset_index(drop=True, inplace=True)
dfFemale[['TC%']]=dfFemale.sort_values(['Year'])[['Total']].pct_change()*100

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(15,4))
plt.plot( 'Year', 'Total', data=dfMale, marker='o', markerfacecolor='blue', markersize=5, color='skyblue', linewidth=4, label="Male")
plt.plot('Year', 'Total', data=dfFemale, marker='o', markerfacecolor='green', markersize=5, color='green', linewidth=4, label="Female")
plt.legend()
plt.xlabel('Year')
plt.ylabel('Total Employed')
plt.title('Annual Employment Across Canada Jan 1976 - Nov 2019')

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(15,4))
plt.plot( 'Year', 'TC%', data=dfMale, marker='o', markerfacecolor='blue', markersize=5, color='skyblue', linewidth=4, label="Male")
plt.plot('Year', 'TC%', data=dfFemale, marker='o', markerfacecolor='green', markersize=5, color='green', linewidth=4, label="Female")
plt.legend()
plt.xlabel('Year')
plt.ylabel('Total Growth Rate')
plt.title('Employment Growth Rate Across Canada Jan 1976 - Nov 2019')

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(15,4))
dfMale = dfMale.iloc[35:]
dfFemale = dfFemale.iloc[35:]
plt.plot( 'Year', 'TC%', data=dfMale, marker='o', markerfacecolor='blue', markersize=5, color='skyblue', linewidth=4, label="Male")
plt.plot('Year', 'TC%', data=dfFemale, marker='o', markerfacecolor='green', markersize=5, color='green', linewidth=4, label="Female")
plt.legend()
plt.xlabel('Year')
plt.ylabel('Total Growth Rate')
plt.title('Annual Growth Rate Across Canada In The Last Decade')

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

import pandas as pd



#load csv file
df=pd.read_csv("netflix_titles.csv") 

#print first 10 rows
print(df.head(10))

#shape of datashape
print(df.shape)

#column names 
print(df.columns)

#data information
print(df.info())

#dataset description(summary) about statistical values like max,min,count,25%,50%,75%,std,mean
print(df.describe())

#check missing value's nummber column wise
print(df.isnull().sum())

#check duplicate value's nummber column wise
print(df.duplicated().sum())

#check country column's first 10 rows
print(df["country"].head(10))
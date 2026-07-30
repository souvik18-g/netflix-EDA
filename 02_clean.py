import pandas as pd


#load dataset
df = pd.read_csv("netflix_titles.csv")

#again check total null in column
print(df.isnull().sum())

#remove duplicate value & non duplicated dataset store in df 
df = df.drop_duplicates()

#fill missing values
df["director"]=df["director"].fillna("unknown")
df["cast"]=df["cast"].fillna("unknown")
df["country"]=df["country"].fillna("unknown")
df["rating"]=df["rating"].fillna("Not_Rated")
df["duration"]=df["duration"].fillna("unknown")

#change data type
df["date_added"] = pd.to_datetime(df["date_added"], format="mixed")
#Now save cleaned data
df.to_csv("netflix_cleaned.csv", index=False)
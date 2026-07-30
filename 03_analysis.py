import pandas as pd

# Load cleaned dataset
df = pd.read_csv("netflix_cleaned.csv")


### Question 1: Which country has the highest number of Netflix titles? ###
#
print(df["country"].value_counts().head())
#
# result:
# here united states have highest no of 2818 titels


### Question 2: Which release year has the highest number of Netflix titles? ###
#
print(df["release_year"].value_counts().head())
#
# result:
#  in year 2018 have highest 1147 release 


### Question 3: Are Movies or TV Shows more common? ###
#
print(df["type"].value_counts())
#
# result:
# mostly (6131) movies in this file is common 


### Question 4: Which content rating appears most frequently?###
#
print(df["rating"].value_counts().head())
#
# result:
# mostly "TV-MA" most frequently appears approx 3207 


### Question 5: Which director has directed the highest number of Netflix titles? ###
#
print(df["director"].value_counts().head())
#
# result:
# actually here unknown directors are directed mostly(2634) because original file their names were not mention 
# but if need to specifically mention the name which have present then i tell  Rajiv Chilaka(18)
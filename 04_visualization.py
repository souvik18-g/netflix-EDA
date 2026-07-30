import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv("netflix_cleaned.csv")


### Chart 1: Top 10 Countries by Netflix Titles
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))

sns.barplot(x=top_countries.index,y=top_countries.values,palette="Blues",edgecolor="black",linewidth=1)

plt.title("Top 10 Countries by Netflix Titles",fontsize=25)
plt.ylabel("Number of Titles",fontsize=15)
plt.xlabel("Country",fontsize=15)

plt.ylim(0,3000)

plt.tight_layout()
plt.savefig("charts/country_titles.png")






### Chart 2: Netflix Titles by Release Year
top_years = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(12,5))
sns.barplot(x=top_years.index, y=top_years.values)

plt.title("Netflix Titles by Release Year",fontsize=25)
plt.xlabel("Release Year",fontsize=15)
plt.ylabel("Number of Titles",fontsize=15)

plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("charts/release_year.png")





### Chart 3: Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="type",hue="type")

plt.title("Movies vs TV Shows",fontsize=25)
plt.xlabel("Content Type",fontsize=15)
plt.ylabel("Count",fontsize=15)

plt.tight_layout()
plt.savefig("charts/movies_vs_tvshows.png")





### Chart 4: Most Common Content Ratings
top_ratings = df["rating"].value_counts()

plt.figure(figsize=(10,5))
sns.barplot(x=top_ratings.index, y=top_ratings.values,palette="Reds")

plt.title("Content Ratings Distribution",fontsize=25)
plt.xlabel("Rating",fontsize=15)
plt.ylabel("Number of Titles",fontsize=15)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/ratings.png")




### Chart 5: Top 10 Directors
top_directors = df["director"].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_directors.values, y=top_directors.index)

plt.title("Top 10 Directors by Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Director")

plt.tight_layout()
plt.savefig("charts/directors.png")

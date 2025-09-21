import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random as ra
import numpy as np

categories = ["Food","Travel","Fashion","Fitness","Music","Culture","Politics","Sports"]
n=500;

dates = pd.date_range("2021-01-01", periods=n)

random_categories = [ra.choice(categories) for _ in range(n)]

likes = np.random.randint(0,10000,size =n)


df = pd.DataFrame({
    "Date": dates,
    "Category" : random_categories,
    "Likes": likes
})

print(df.head())

print(df.info())

print(df.describe())

print(df["Category"].value_counts())

#cleaning
df = df.dropna()
df = df.drop_duplicates()


df["Date"] = pd.to_datetime(df["Date"])
df["Likes"] = df["Likes"].astype(int)

sns.distplot(df["Likes"],bins =20)

plt.title("Distribution of Likes")
plt.xlabel("Number of Likes")
plt.ylabel("Count")

plt.show()

sns.boxplot(x="Category",y="Likes",data=df)
plt.title("Likes Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Number of Likes")
plt.xticks(rotation =45)
plt.show()


mean_likes = df["Likes"].mean()
print("Mean of all Likes:",mean_likes)


mean_per_category = df.groupby("Category")["Likes"].mean()
print("Mean Likes per Category:")
print(mean_per_category)


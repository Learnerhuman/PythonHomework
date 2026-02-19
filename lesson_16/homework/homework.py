#part1
import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

customers_df = pd.read_sql("SELECT * FROM customers", conn)
customers_df.head(10)

iris_df = pd.read_json("iris.json")

print(iris_df.shape)
print(iris_df.columns)

titanic_df = pd.read_excel("titanic.xlsx")
titanic_df.head()

flights_df = pd.read_parquet("flights.parquet")
flights_df.info()

movie_df = pd.read_csv("movie.csv")
movie_df.sample(10)


#part2
iris_df.columns = iris_df.columns.str.lower()


iris_df[["sepal_length", "sepal_width"]]

titanic_df[titanic_df["Age"] > 30]

titanic_df["Sex"].value_counts()

flights_df[["origin", "dest", "carrier"]]

flights_df["dest"].nunique()

long_movies = movie_df[movie_df["duration"] > 120]

long_movies.sort_values(
    by="director_facebook_likes",
    ascending=False
)

#part3


iris_df.agg(["mean", "median", "std"])

titanic_df["Age"].agg(["min", "max", "sum"])

movie_df.groupby("director_name")["director_facebook_likes"] \
        .sum() \
        .sort_values(ascending=False) \
        .head(1)

movie_df.sort_values("duration", ascending=False) \
        [["movie_title", "director_name", "duration"]] \
        .head(5)

flights_df.isna().sum()
flights_df["dep_delay"].fillna(
    flights_df["dep_delay"].mean(),
    inplace=True
)

#task1
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("chinook.db")

# Load tables
customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)

# Inner join
merged = pd.merge(customers, invoices, on="CustomerId", how="inner")

# Total invoices per customer
invoice_count = (
    merged.groupby("CustomerId")
          .size()
          .reset_index(name="Total_Invoices")
)

print(invoice_count.head())
#task2
movies = pd.read_csv("movie.csv")

df1 = movies[["director_name", "color"]]
df2 = movies[["director_name", "num_critic_for_reviews"]]

# Left join
left_join = pd.merge(df1, df2, on="director_name", how="left")

# Full outer join
outer_join = pd.merge(df1, df2, on="director_name", how="outer")

print("Left Join Rows:", len(left_join))
print("Outer Join Rows:", len(outer_join))

#Titanic Grouped Aggregations

titanic = pd.read_csv("titanic.csv")

grouped = (
    titanic.groupby("Pclass")
           .agg(
               Average_Age=("Age", "mean"),
               Total_Fare=("Fare", "sum"),
               Passenger_Count=("PassengerId", "count")
           )
           .reset_index()
)

print(grouped)
#Multi-level Grouping on Movie Data

movie_grouped = (
    movies.groupby(["color", "director_name"])
          .agg(
              Total_Reviews=("num_critic_for_reviews", "sum"),
              Avg_Duration=("duration", "mean")
          )
          .reset_index()
)

print(movie_grouped.head())
#Nested Grouping on Flights

flights = pd.read_csv("flights.csv")

flight_grouped = (
    flights.groupby(["Year", "Month"])
           .agg(
               Total_Flights=("FlightNum", "count"),
               Avg_ArrDelay=("ArrDelay", "mean"),
               Max_DepDelay=("DepDelay", "max")
           )
           .reset_index()
)

print(flight_grouped.head())
#Custom Function on Titanic

def classify_age(age):
    if pd.isna(age):
        return "Unknown"
    elif age < 18:
        return "Child"
    else:
        return "Adult"

titanic["Age_Group"] = titanic["Age"].apply(classify_age)
#Normalize Employee Salaries (Within Department)

employee = pd.read_csv("employee.csv")

employee["Normalized_Salary"] = (
    employee.groupby("Department")["Salary"]
            .transform(lambda x: (x - x.min()) / (x.max() - x.min()))
)

print(employee.head())
#Custom Function on Movies

def classify_duration(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"

movies["Length_Category"] = movies["duration"].apply(classify_duration)
#Titanic Pipeline

def filter_survived(df):
    return df[df["Survived"] == 1]

def fill_age(df):
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df

def create_fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

titanic_pipeline = (
    titanic.pipe(filter_survived)
           .pipe(fill_age)
           .pipe(create_fare_per_age)
)

print(titanic_pipeline.head())
#Flights Pipeline

def filter_delay(df):
    return df[df["DepDelay"] > 30]

def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / (df["AirTime"] / 60)
    return df

flights_pipeline = (
    flights.pipe(filter_delay)
           .pipe(add_delay_per_hour)
)

print(flights_pipeline.head())

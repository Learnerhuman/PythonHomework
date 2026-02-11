#task1
from bs4 import BeautifulSoup

# Load HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find("tbody").find_all("tr")

weather_data = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.replace("°C", ""))
    condition = cols[2].text.strip()

    weather_data.append({
        "day": day,
        "temperature": temp,
        "condition": condition
    })

# Display weather data
print("5-Day Weather Forecast:")
for w in weather_data:
    print(f"{w['day']} - {w['temperature']}°C - {w['condition']}")

# Highest temperature
max_temp = max(w["temperature"] for w in weather_data)
hot_days = [w["day"] for w in weather_data if w["temperature"] == max_temp]

print("\nHighest Temperature:")
print(f"{max_temp}°C on {', '.join(hot_days)}")

# Sunny days
sunny_days = [w["day"] for w in weather_data if w["condition"] == "Sunny"]
print("\nSunny Days:")
print(", ".join(sunny_days))

# Average temperature
avg_temp = sum(w["temperature"] for w in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {avg_temp:.2f}°C")


#task2

import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    link TEXT,
    UNIQUE(title, company, location)
)
""")

conn.commit()
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()
    link = job.find("a", string="Apply")["href"]

    cursor.execute("""
    SELECT description, link FROM jobs
    WHERE title=? AND company=? AND location=?
    """, (title, company, location))

    existing = cursor.fetchone()

    if existing:
        if existing[0] != description or existing[1] != link:
            cursor.execute("""
            UPDATE jobs
            SET description=?, link=?
            WHERE title=? AND company=? AND location=?
            """, (description, link, title, company, location))
    else:
        cursor.execute("""
        INSERT INTO jobs (title, company, location, description, link)
        VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, description, link))

conn.commit()
import csv

def export_jobs(filter_value, by="location"):
    query = f"SELECT title, company, location, description, link FROM jobs WHERE {by}=?"
    cursor.execute(query, (filter_value,))
    rows = cursor.fetchall()

    with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Description", "Link"])
        writer.writerows(rows)

# Example usage
export_jobs("New York", by="location")


#task3
import requests
import json

url = "https://api.demoblaze.com/bycat"
payload = {"cat": "laptop"}

response = requests.post(url, json=payload)
data = response.json()["Items"]

laptops = []

for item in data:
    laptops.append({
        "name": item["title"],
        "price": item["price"],
        "description": item["desc"]
    })

with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4, ensure_ascii=False)

print("Laptop data saved to laptops.json")



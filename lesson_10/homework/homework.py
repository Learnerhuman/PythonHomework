#Task1
import requests

API_KEY = "YOUR_API_KEY_HERE"
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error fetching weather data")
#task2
import requests
import random

API_KEY = "YOUR_TMDB_API_KEY"

# Step 1: Get available genres
genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
genre_response = requests.get(genre_url)
genres = genre_response.json()["genres"]

# Convert genres to dictionary
genre_dict = {genre["name"].lower(): genre["id"] for genre in genres}

# Step 2: Ask user for genre
user_genre = input("Enter movie genre (e.g. Action, Comedy, Drama): ").lower()

if user_genre not in genre_dict:
    print("Genre not found!")
else:
    genre_id = genre_dict[user_genre]

    # Step 3: Fetch movies by genre
    movie_url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    movie_response = requests.get(movie_url)
    movies = movie_response.json()["results"]

    if movies:
        movie = random.choice(movies)
        print("\n🎬 Recommended Movie:")
        print(f"Title: {movie['title']}")
        print(f"Release Date: {movie['release_date']}")
        print(f"Rating: {movie['vote_average']}")
        print(f"Overview: {movie['overview']}")
    else:
        print("No movies found for this genre.")

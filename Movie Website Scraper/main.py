import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/",headers=headers)
website = response.text
#print(website)

soup = BeautifulSoup(website,"html.parser")

#print(soup.prettify())

movie_list = soup.select("span h2 strong")
movie_titles = [movie.getText() for movie in movie_list]

#for i in range(len(movie_titles)-1 ,0, -1):
#    print(movie_titles[i])

movies = movie_titles[::-1]
with open("top 100 movies of all the time.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


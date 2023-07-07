import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content,"html.parser")

movies = soup.find_all(name="h3",class_="title")
movies = [movie.getText() for movie in movies]
movies.reverse()
print(movies)

with open(file="movies.txt",mode="w",encoding='UTF8') as file:
    for movie in movies:
        file.write(movie)
        file.write("\n")




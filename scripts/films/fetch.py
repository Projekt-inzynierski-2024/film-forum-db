import requests
import jsonpickle
from bs4 import BeautifulSoup, Tag
import re

# needs top500.py script to be run first

# get urls

urls = []

with open("urls.txt", "r") as urls_file:
    for line in urls_file:
        urls.append(line[:-1])


# film representation

class Film(object):
    def __init__(self, title:str, description: str, year: int, directors: list[str], actors: list[str], length: str) -> None:
        self.title = title
        self.description = description
        self.year = year
        self.directors = directors
        self.actors = actors
        self.length = self.__parseLength(length)

    def __parseLength(self, length: str) -> int:
        regex = r"^([0-9]*)h ([0-9]*)m"
        matches = re.finditer(regex, length, re.MULTILINE)

        minutes = 0
        for m in matches:
            for i, g in enumerate(m.groups()):
                if i == 0:
                    minutes += int(g) * 60
                else:
                    minutes += int(g)

        return minutes

# session 

session = requests.Session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en"
}

# fetch data

films = []

for i, url in enumerate(urls):
    print("Fetching " + url + "... (" + str(i + 1) + "/" + str(len(urls)) + ")")

    shorturl = url.split("https://www.imdb.com")[-1]

    response = session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("h1", {"data-testid": "hero__pageTitle"}).findChild("span").text
    description = soup.find("span", {"data-testid": "plot-l"}).text

    year_a = soup.find("a", {"href": shorturl + "releaseinfo?ref_=tt_ov_rdat" })
    year = year_a.text

    directors_list = soup.find("span", {"aria-label":"See full cast and crew"}).find_parent("li").find("div", class_="ipc-metadata-list-item__content-container").findAll("li")
    directors = [dir.find("a").text for dir in directors_list]

    actors_list = soup.find("a", {"href":shorturl + "fullcredits/cast?ref_=tt_ov_st_sm"}).find_parent("li").find("div", class_="ipc-metadata-list-item__content-container").findAll("li")
    actors = [act.find("a").text for act in actors_list]

    length = year_a.findParent("ul").findAll("li")[-1].text

    films.append(Film(title, description, int(year), directors, actors, length))

# save data

json_data = jsonpickle.encode(films, unpicklable=False)

with open("films.json", "w") as films_json:
    films_json.write(json_data)

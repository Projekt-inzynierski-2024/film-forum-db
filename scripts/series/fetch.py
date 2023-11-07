import re
import requests
from bs4 import BeautifulSoup
import jsonpickle


class Episode:
    def __init__(self, title: str, description: str, year: int, length: str, episodeNumber: int, seasonNumber: int, actors: list[str], directors: list[str]) -> None:
        self.title = title
        self.description = description
        self.year = year
        self.episodeNumber = episodeNumber
        self.seasonNumber = seasonNumber
        self.directors = directors
        self.actors = actors
        self.length = self.__parseLength(length)

    def __parseLength(self, length: str) -> int:
        regex = r"(([0-9]*)h )?([0-9]*)m"
        matches = re.finditer(regex, length, re.MULTILINE)

        minutes = 0
        for m in matches:
            for i, g in enumerate(m.groups()):
                if g is not None:
                    if i == 1:
                        minutes += 60 * int(g)
                    elif i == 2:
                        minutes += int(g)
        return minutes


class Film:
    def __init__(self, title: str, description: str, episodes: list[Episode]) -> None:
        self.title = title
        self.description = description
        self.episodes = episodes


series = [
    "https://www.imdb.com/title/tt0903747/", # breaking bad
    "https://www.imdb.com/title/tt0386676/", # the office
    "https://www.imdb.com/title/tt5348176/", # barry
    "https://www.imdb.com/title/tt5071412/",  # ozark
]

session = requests.Session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en"
}

films: list[Film] = []

for ui, url in enumerate(series):
    print("Fetching serie... (" + str(ui + 1) + "/" + str(len(series)) + ")")
    response = session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find(
        "h1", {"data-testid": "hero__pageTitle"}).findChild("span").text

    description = soup.find("span", {"data-testid": "plot-l"}).text
    episodes: list[Episode] = []

    e_url = url + "episodes"

    response = session.get(e_url)
    soup = BeautifulSoup(response.content, "html.parser")

    seasons = len(soup.findAll("li", {"data-testid": "tab-season-entry"}))

    for seasonNumber in range(1, seasons + 1):
        print(" Fetching season... (" + str(seasonNumber) + "/" + str(seasons) + ")")

        if seasonNumber > 1:
            response = session.get(e_url + "/?season=" + str(seasonNumber))
            soup = BeautifulSoup(response.content, "html.parser")

        episode_articles = soup.findAll(
            "article", class_="episode-item-wrapper")

        for episodeNumber, article in enumerate(episode_articles):
            print("     Fetching episode... (" + str(episodeNumber + 1) +
                  "/" + str(len(episode_articles)) + ")")
            title_div = article.find("div", class_="ipc-title__text")
            ep_title = title_div.text.split(" ∙ ")[-1]
            ep_description = article.find(
                "div", class_="ipc-html-content-inner-div").text

            year = title_div.find_parent("h4").parent()[-1].text.split(" ")[-1]

            shorturl = article.find("a")["href"]
            ep_url = "https://imdb.com" + shorturl
            ep_res = session.get(ep_url)
            ep_soup = BeautifulSoup(ep_res.content, "html.parser")

            directors_list = ep_soup.find("span", {"aria-label": "See full cast and crew"}).find_parent(
                "li").find("div", class_="ipc-metadata-list-item__content-container").findAll("li")
            directors = [dir.find("a").text for dir in directors_list]

            actors_href = shorturl.split(
                "?ref")[0] + "fullcredits/cast?ref_=tt_ov_st_sm"

            actors_list = ep_soup.find("a", {"href": actors_href}).find_parent(
                "li").find("div", class_="ipc-metadata-list-item__content-container").findAll("li")
            actors = [act.find("a").text for act in actors_list]

            length = ep_soup.find("h1", {"data-testid": "hero__pageTitle"}).find_parent(
                "div").findChild("ul").findAll("li")[-1].text

            episodes.append(Episode(ep_title, ep_description,
                            year, length, episodeNumber + 1, seasonNumber, actors, directors))

    film = Film(title, description, episodes)
    films.append(film)

series_json = jsonpickle.encode(films, unpicklable=False)

with open("series.json", "w") as series_file:
    series_file.write(series_json)

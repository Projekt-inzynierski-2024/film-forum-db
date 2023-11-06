import requests
from bs4 import BeautifulSoup

top_url="https://www.imdb.com/list/ls050782187/?sort=list_order,asc&st_dt=&mode=detail&page="

urls = []

for page in range(1, 6):
    print("Fetching page " + str(page) + "...")
    p_url = top_url + str(page)

    response = requests.get(p_url)

    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("h3", class_="lister-item-header")

    for item in items:
        urls.append("https://www.imdb.com" + item.find("a")["href"] + "\n")

with open("urls.txt", "w") as urls_file:
    urls_file.writelines(urls)

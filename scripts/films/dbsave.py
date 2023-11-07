# requires top500.py and fetch.py scripts to be run before

import sys
import json
from pymongo import MongoClient

if len(sys.argv) < 3:
    print("2 arguments are required: <login> <password>")
    exit(1)

login = sys.argv[1]
password = sys.argv[2]

with open("films.json", "r") as json_file:
    json_str = json_file.read()

films: list = json.loads(json_str)

actors: set[str] = set(sum([film["actors"] for film in films], []))
directors: set[str] = set(sum([film["directors"] for film in films], []))

def parse_humans(human_set: set[str]) -> list:
    humans_obj = []

    for human in human_set:
        try:
            space_id = human.index(" ")
            name = human[:space_id]
            surname = human[space_id + 1:]
            humans_obj.append({"name": name, "surname" : surname})
        except:
            humans_obj.append({"name": human})
            
    return humans_obj

actors_objs = parse_humans(actors)
directors_objs = parse_humans(directors)

client = MongoClient("mongodb://" + login + ":"+ password +"@127.0.0.1:27017")
db = client["filmForum"]

def insert_humans(humans_objs: list, table_name: str):
    humans_id = dict()

    for human in humans_objs:
        inserted = db[table_name].insert_one(human)
        fullname = human["name"]
        
        if human.get("surname") != None:
            fullname += " " + human["surname"]

        humans_id[fullname] = inserted.inserted_id

    return humans_id

actors_ids = insert_humans(actors_objs, "actor")
directors_ids = insert_humans(directors_objs, "director")

for film in films:
    film_obj = {
            "title": film["title"],
            "description": film["description"],
            "isMovie": True
    }

    inserted_film = db.film.insert_one(film_obj)

    episode = {
        "actorIds": [actors_ids[a] for a in film["actors"]],
        "directorIds": [directors_ids[a] for a in film["directors"]],
        "filmId": inserted_film.inserted_id,
        "length": film["length"],
        "year": film["year"],
        "episodeNumber": 0,
        "seasonNumber": 0
    }

    db.episode.insert_one(episode)


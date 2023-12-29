import requests
import json
import uuid
import string
import random


url = "http://127.0.0.1:80"
session = requests.Session()
session.headers.update({"Content-Type": "application/json"})
unique = str(uuid.uuid4())


def rand_str(n: int):
    ll = ''.join(random.choice(string.ascii_lowercase)
                 for _ in range(int(n / 3)))

    ul = ''.join(random.choice(string.ascii_uppercase)
                 for _ in range(int(n / 3)))

    digits = ''.join(random.choice(string.digits) for _ in range(int(n / 3)))

    password_range = ll + ul + digits

    password = ''.join(random.sample(password_range, len(password_range)))
    password += ''.join(random.sample(string.punctuation, (n - len(password))))

    return password


def login(email, password):
    login_url = f"{url}/login"
    body = {"email": email, "password": password}
    result = session.post(login_url, json.dumps(body))
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = dict()
        obj["jwt"] = None
        print(result.text)
    return (result.status_code, obj["jwt"])


def register(username, email, password):
    register_url = f"{url}/register"
    body = {"username": username, "email": email,
            "password": password, "confirmPassword": password}
    result = session.post(register_url, json.dumps(body))
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = dict()
        obj["jwt"] = None
        print(result.text)
    return (result.status_code, obj["jwt"])


def get_films():
    films_url = f"{url}/api/film"
    result = session.get(films_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None
        print(result.text)
    return (result.status_code, obj)


def create_film(title, description):
    film_url = f"{url}/api/film"
    body = {"title": title, "description": description}
    result = session.post(film_url, json.dumps(body))
    return result.status_code


def update_film(id, title, description):
    film_url = f"{url}/api/film/{id}"
    body = {"title": title, "description": description}
    result = session.put(film_url, json.dumps(body))
    return result.status_code


def get_film(id):
    film_url = f"{url}/api/film/{id}"
    result = session.get(film_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None
    return (result.status_code, obj)


def get_episodes():
    episodes_url = f"{url}/api/episode"
    result = session.get(episodes_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None
        print(result.text)
    return (result.status_code, obj)


def create_episode(title, description, film_id):
    episode_url = f"{url}/api/episode"
    body = {"title": title, "description": description, "filmId": film_id}
    result = session.post(episode_url, json.dumps(body))
    return result.status_code


def update_episode(id, title, description, film_id):
    episode_url = f"{url}/api/episode/{id}"
    body = {"title": title, "description": description, "filmId": film_id}
    result = session.put(episode_url, json.dumps(body))
    return result.status_code


def get_episode(id):
    episode_url = f"{url}/api/episode/{id}"
    result = session.get(episode_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None
    return (result.status_code, obj)


def get_directors():
    director_url = f"{url}/api/director"
    result = session.get(director_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None

    return (result.status_code, obj)


def create_director(name, surname, description):
    director_url = f"{url}/api/director"
    body = {"name": name, "surname": surname, "description": description}
    result = session.post(director_url, json.dumps(body))
    return result.status_code


def update_director(id, name, surname, description):
    director_url = f"{url}/api/director/{id}"
    body = {"name": name, "surname": surname, "description": description}
    result = session.put(director_url, json.dumps(body))
    return result.status_code


def get_director(id):
    director_url = f"{url}/api/director/{id}"
    result = session.get(director_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None
    return (result.status_code, obj)


def get_actors():
    actor_url = f"{url}/api/actor"
    result = session.get(actor_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None

    return (result.status_code, obj)


def create_actor(name, surname, description):
    actor_url = f"{url}/api/actor"
    body = {"name": name, "surname": surname, "description": description}
    result = session.post(actor_url, json.dumps(body))
    return result.status_code


def update_actor(id, name, surname, description):
    actor_url = f"{url}/api/actor/{id}"
    body = {"name": name, "surname": surname, "description": description}
    result = session.put(actor_url, json.dumps(body))
    return result.status_code


def get_actor(id):
    actor_url = f"{url}/api/actor/{id}"
    result = session.get(actor_url)
    try:
        obj = json.loads(result.text)
    except Exception:
        obj = None
    return (result.status_code, obj)


def test(header, code, valid):
    if valid:
        print(header + ":", code, " VALID")
    else:
        print(header + ":", code, " INVALID")
        exit(-1)


username = unique
email = f"{unique}@mail.com"
password = rand_str(10)

# users

(code, _) = register(username, email, password)

test("REGISTER", code, code == 201)

(code, jwt) = login(email, password)

test("LOGIN", code, code == 200)

session.headers.update({"Authorization": f"Bearer {jwt}"})

# 2fa

# films

code = create_film("Test", "Testowy film")

test("CREATE FILM", code, code == 201)

(code, films) = get_films()

test("FILMS", code, code == 200)

film_id = films[-1]["id"]

code = update_film(film_id, "Test updated", "Testowy film edytowany")

test("UPDATE FILM", code, code == 204)

(code, film) = get_film(film_id)

test("GET FILM", code, code == 200)

# episodes

code = create_episode("Tytuł", "Opis", film_id)

test("CREATE EPISODE", code, code == 201)

(code, episodes) = get_episodes()

test("EPISODES", code, code == 200)

episode_id = episodes[-1]["id"]

code = update_episode(episode_id, "Tytuł updated", "Opis edytowany", film_id)

test("UPDATE EPISODE", code, code == 204)

(code, episode) = get_episode(episode_id)

test("GET EPISODE", code, code == 200)

# directors

code = create_director("jan", "kowalski", "jest reżyserem")

test("CREATE DIRECTOR", code, code == 201)

(code, directors) = get_directors()

test("DIRECTORS", code, code == 200)

director_id = directors[-1]["id"]

code = update_director(director_id, "jan", "kowal", "jestem reżyserem")

test("UPDATE DIRECTOR", code, code == 204)

(code, director) = get_director(director_id)

test("GET DIRECTOR", code, code == 200)

# actors

code = create_actor("jan", "kowalski", "Jest aktorem")

test("CREATE ACTOR", code, code == 201)

(code, actors) = get_actors()

test("ACTORS", code, code == 200)

actor_id = actors[-1]["id"]

code = update_actor(actor_id, "jan", "kowal", "Jestem aktorem")

test("UPDATE ACTOR", code, code == 204)

(code, actor) = get_actor(actor_id)

test("GET ACTOR", code, code == 200)

# reviews

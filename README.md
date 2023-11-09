# film-forum-db
SQL/noSQL queries for FilmForum databases

## mongo docker

Aby odpalić baze mongo oraz interfejs mongo-express:
 - Sklonuj to repo
 - wejdź do głównego folderu `film-forum-db/`
 - utwórz plik `.env`, w którym umieścisz hasła do bazy np.:

```bash
MONGODB_PASSWORD="123456" # hasło do bazy dla użytkownika root
EXPRESS_PASSWORD="123456" # hasło do interfejsu web dla użytkownika admin
MSSQL_SA_PASSWORD="zaq1@WSX" # hasło do bazy mssql (musi być 'trudne' inaczej docker nie odpali)
```
 
 - uruchom kontenery za pomocą komendy

 ```
docker compose -f docker-compose.yml up -d
 ```

 - Connection string do bazy `root:123456@localhost:27017`
 - interfejs web : `http://localhost:8081`

# film-forum-db
SQL/noSQL queries for FilmForum databases

## bazy

Aby odpalić baze mongo, interfejs mongo-express oraz bazę mssql:
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

 - interfejs web : `http://localhost:8081`

 - Connection string do bazy mongo: `root:123456@localhost:27017`
 - Connection string do bazy mssql: `Server=localhost;Database=UsersDb;Uid=SA;Pwd=zaq1@WSX;TrustServerCertificate=True`

## bazy testowe

 - Connection string do bazy mongo-tests: `root:123456@localhost:37017`
 - Connection string do bazy mssql-tests: `Server=localhost,2433;Database=UsersDb;Uid=SA;Pwd=zaq1@WSX;TrustServerCertificate=True`


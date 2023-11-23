# film-forum-db
SQL/noSQL queries for FilmForum databases

## Databases

To run MongoDB database, mongo-express interface and MS SQL database:
 - Clone this repository
 - Enter main directory `film-forum-db/`
 - Create a file `.env`, and paste databases' passwords for example.:

```bash
MONGODB_PASSWORD="123456" # password to access user interface for root
EXPRESS_PASSWORD="123456" # password to access user interface for admin
MSSQL_SA_PASSWORD="zaq1@WSX" # password for ms sql database (must be difficult otherwise it won't run)
```
 
 - run the containers using command

 ```
docker compose -f docker-compose.yml up -d
 ```

## Productions databases
 - web interface : `http://localhost:8081`

 - Connection string to MongoDB database: `root:123456@localhost:27017`
 - Connection string to MS SQL database: `Server=localhost,1433;Database=UsersDb;Uid=SA;Pwd=zaq1@WSX;TrustServerCertificate=True`

## Testing databases

 - Connection string to MongoDB database: `root:123456@localhost:37017`
 - Connection string to MS SQL database: `Server=localhost,2433;Database=UsersDb;Uid=SA;Pwd=zaq1@WSX;TrustServerCertificate=True`


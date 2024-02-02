# film-forum-db

Docker containers for film-forum databases and api.

## Databases

To run MongoDB database, mongo-express interface and MS SQL database:
 - Clone this repository
 - Enter main directory `film-forum-db/`
 - Create a file `.env`, and paste databases' passwords for example.:

```bash
MONGODB_USERNAME="root" # mongodb username
MONGODB_PASSWORD="zaq1@WSX" # mongodb password
EXPRESS_USERNAME="root" # mongo express username
EXPRESS_PASSWORD="zaq1@WSX" # mongo express password
MSSQL_SA_PASSWORD="zaq1@WSX" # password for ms sql database (must be difficult otherwise it won't run)
```
 
 - run containers using commands:

 ```
 # for testing

 docker compose -f docker-compose.yml up -d mongo mongo-tests mongo-express mssql mssql-tests

 # for development

 docker compose -f docker-compose.yml up -d mongo mssql

 # for production
 # api container is listening on port 80

 docker compose -f docker-compose.yml up -d mongo mssql api

 ```

## Mongo web interface

  Mongo express is web interface for mongo db. It's suitable for testing and works here -> `http://localhost:8081`

## Production databases

 - Connection string to MongoDB database: `root:123456@localhost:27017`
 - Connection string to MS SQL database: `Server=localhost,1433;Database=UsersDb;Uid=SA;Pwd=zaq1@WSX;TrustServerCertificate=True`

## Testing databases

 - Connection string to MongoDB database: `root:123456@localhost:37017`
 - Connection string to MS SQL database: `Server=localhost,2433;Database=UsersDb;Uid=SA;Pwd=zaq1@WSX;TrustServerCertificate=True`

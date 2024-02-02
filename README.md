# film-forum-db

Docker containers for film-forum databases and api.

## Installation

 1. Clone this repository
 2. Enter `film-forum-db/` directory
 3. Create a `.env` file with passwords e.g.:

```bash
MONGODB_USERNAME="root" # mongodb username
MONGODB_PASSWORD="zaq1@WSX" # mongodb password
EXPRESS_USERNAME="root" # mongo express username
EXPRESS_PASSWORD="zaq1@WSX" # mongo express password
MSSQL_SA_PASSWORD="zaq1@WSX" # password for ms sql database (must be difficult otherwise it won't run)
```
 
 4. run docker containers 

 ```
 # for testing

 docker compose -f docker-compose.yml up -d mongo mongo-tests mongo-express mssql mssql-tests

 # for development

 docker compose -f docker-compose.yml up -d mongo mssql

 # for production
 # api container is listening on port 80

 docker compose -f docker-compose.yml up -d mongo mssql api

 ```

## Requirements

This repo uses latest mongo container which requires CPU with AVX support.
There may be some issues while running mssql container on linux with kernel >= 6.7 (see [https://github.com/microsoft/mssql-docker/issues/868](https://github.com/microsoft/mssql-docker/issues/868))

## LICENSE

[MIT](./LICENSE)

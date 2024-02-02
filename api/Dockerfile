FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env

RUN apt update && apt install -y git
RUN git clone https://github.com/Projekt-inzynierski-2024/film-forum-api.git /app

WORKDIR /app/src/FilmForumWebAPI

ENV MONGODB_USERNAME=root
ENV MONGODB_PASSWORD=zaq1@WSX
ENV MSSQL_SA_PASSWORD=zaq1@WSX

RUN export FilmForumMongoDatabase__ConnectionString="mongodb://$MONGODB_USERNAME:$MONGODB_PASSWORD@mongo:27017"
RUN export ConnectionStrings__UsersDbConnection="Server=mssql,1433;Database=UsersDb;Uid=SA;Pwd=$MSSQL_SA_PASSWORD;TrustServerCertificate=True"

RUN dotnet restore
RUN dotnet publish -c Release -o /out

FROM  mcr.microsoft.com/dotnet/aspnet:7.0

WORKDIR /app
COPY --from=build-env /out .

EXPOSE 80

ENTRYPOINT ["dotnet", "FilmForumWebAPI.dll"]

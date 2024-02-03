FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env

RUN apt update && apt install -y git
RUN git clone https://github.com/Projekt-inzynierski-2024/film-forum-api.git /app

WORKDIR /app/src/FilmForumWebAPI

RUN dotnet restore
RUN dotnet publish -c Release -o /out

FROM  mcr.microsoft.com/dotnet/aspnet:7.0

WORKDIR /app
COPY --from=build-env /out .

EXPOSE 80

ENTRYPOINT ["dotnet", "FilmForumWebAPI.dll"]

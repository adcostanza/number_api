FROM microsoft/aspnetcore-build:1.0 as build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY *.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY . ./
RUN dotnet ef migrations add "First Migration"
RUN dotnet ef database update 
RUN dotnet publish -c Release -o out

# Builvdruntime image
FROM microsoft/aspnetcore:1.0
WORKDIR /app
COPY --from=build-env /app/out ./

ENV ASPNETCORE_URLS http://+:5000
EXPOSE 5000
ENTRYPOINT ["dotnet", "phone-api.dll", "--server.urls", "http://0.0.0.0:5000"]

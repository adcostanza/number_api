docker stop $(docker ps -q)
docker run -p 5000:5000 -t core

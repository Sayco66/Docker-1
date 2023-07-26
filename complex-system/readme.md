#### Création du volume
docker volume create storage

### Build et run du scraper
docker build -t scraper .
docker run -v storage:/usr/src/app/data scraper

### Build et run du cleaner
docker build -t cleaner .
docker run -v storage:/usr/src/app/data cleaner
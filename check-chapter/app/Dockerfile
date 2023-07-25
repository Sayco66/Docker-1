# On part de l'image python:3.9-slim
FROM python:3.9-slim 

# On se place dans ce dossier dans le conteneur
WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py
# On part de l'image python:3.9-slim
FROM python:3.9-slim 

# On se place dans ce dossier dans le conteneur
WORKDIR /usr/src/app

COPY check_chapter.py .

RUN pip3 install requests

CMD ["python", "check_chapter.py"]
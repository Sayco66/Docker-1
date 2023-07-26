FROM python:3.9-slim

WORKDIR /opt/demo/

# copy whole app while being inside the folder (Dockerfile in this folder)
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py
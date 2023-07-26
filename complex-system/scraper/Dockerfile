FROM python:3.9-slim 

WORKDIR /usr/src/app

COPY scraper.py .

RUN pip3 install lxml
RUN pip3 install pandas

CMD ["python", "scraper.py"]
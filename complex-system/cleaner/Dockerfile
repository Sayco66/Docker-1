FROM python:3.9-slim 

WORKDIR /usr/src/app

COPY cleaner.py .

RUN pip3 install pandas

CMD ["python", "cleaner.py"]
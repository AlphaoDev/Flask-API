FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY client.py client.py

COPY entrypoint.sh entrypoint.sh
RUN ["chmod","+x","entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
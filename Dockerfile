FROM python:3.7
RUN apt-get update -y
RUN apt-get upgrade -y

COPY . /app
WORKDIR /app

ENV API inbox-server.py

RUN pip install -r requirments.txt
RUN pip install gunicorn

EXPOSE 8080

ENTRYPOINT ["gunicorn", "inbox-server:app"]


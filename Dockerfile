FROM python:3.8-slim
RUN apt-get update -y
RUN apt-get dist-upgrade -y

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirments.txt
RUN pip install gunicorn

ENV CATCHALL_HOSTNAME = ""
ENV CATCHALL_USERNAME = ""
ENV CATCHALL_PASSWORD = ""

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "catchallinbox:app"]

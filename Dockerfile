FROM python:latest

RUN apt update -y
RUN apt install gcc libmariadb3 libmariadb-dev mariadb-client sqlite3 libsqlite3-dev openssl -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

EXPOSE 3306/tcp
EXPOSE 5000/tcp
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

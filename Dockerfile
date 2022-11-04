FROM python:latest

RUN apt update -y

RUN sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
RUN curl -LsS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
RUN apt install gcc libmariadb3 libmariadb-dev mariadb-client sqlite3 libsqlite3-dev openssl -y

RUN sudo apt-get update
RUN sudo apt-get upgrade

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

EXPOSE 3306/tcp
EXPOSE 5000/tcp
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

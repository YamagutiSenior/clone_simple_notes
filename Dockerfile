FROM python:latest

RUN apt update -y
RUN apt install sqlite3 libsqlite3-dev -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

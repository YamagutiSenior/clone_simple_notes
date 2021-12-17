FROM python:3-alpine

RUN apk update
RUN apk add mariadb-connector-c-dev
RUN apk add mariadb-connector-c
RUN apk add mariadb-client

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

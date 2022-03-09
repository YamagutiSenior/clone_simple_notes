FROM python:latest

RUN apt update
RUN apt install libmariadb3 libmariadb-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

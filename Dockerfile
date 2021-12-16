FROM python:3-alpine

RUN apk update

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

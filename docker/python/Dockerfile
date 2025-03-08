FROM python:3.8

ADD . /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ./wait-for-it.sh db:3306 -- python app.py

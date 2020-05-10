FROM python:3.6.1-alpine

WORKDIR /app

ADD Pipfile Pipfile.lock ./
RUN pip3 install pipenv
RUN pipenv install

ADD . .

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    CONNECT_AUTH_TYPE=in \
    KAT_ENV=production \
    FLASK_ENV=production

EXPOSE 5000

CMD ["pipenv", "run", "python3", "app.py"]
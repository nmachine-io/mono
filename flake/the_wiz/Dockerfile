FROM python:3.6.1
WORKDIR /app

RUN pip3 install pipenv
ADD Pipfile Pipfile.lock /app/
RUN pipenv lock --clear -r > requirements.txt
RUN pip3 install -r requirements.txt

ENV KAT_ENV=production
ENV FLASK_ENV=production
ENV CONNECT_TYPE=in

ADD . /app/
ENTRYPOINT ["python3", "/app/main.py"]
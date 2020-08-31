FROM python:3.6.1
WORKDIR /app
RUN pip3 install pipenv
ADD Pipfile Pipfile.lock /app/
RUN pipenv lock -r > requirements.txt
RUN pip3 install -r requirements.txt
ADD . /app/
ENTRYPOINT ['python3', 'main.rb']
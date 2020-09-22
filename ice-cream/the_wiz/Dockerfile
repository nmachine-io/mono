FROM python:3.6.1

RUN apt-get update && apt-get install -y curl apt-transport-https
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" |  tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update && apt-get install -y kubectl

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

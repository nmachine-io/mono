FROM ruby:2.6.3
WORKDIR /app

RUN apt-get update && apt-get install -y curl wget

ENV TAM_CMD="/app/local-eval.sh"

RUN wget -q https://get.helm.sh/helm-v3.4.0-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
  && chmod +x /usr/local/bin/helm

RUN  wget -q https://github.com/nectar-cs/tam_server/releases/download/1.0.3/tam_server.tar.gz \
  && tar -xf tam_server.tar.gz \
  && mv tam_server /usr/local/bin/tam_server \
  && chmod +x /usr/local/bin/tam_server

ADD . .

FROM ubuntu
WORKDIR /app

RUN apt-get update && apt-get install -y curl wget

ENV KTEA_EXECUTABLE="/app/local-eval.sh"

RUN wget -q https://get.helm.sh/helm-v3.4.0-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
  && chmod +x /usr/local/bin/helm

RUN wget -q https://github.com/nmachine-io/ktea-executable-server/releases/download/1.0.8/ktea-executable-server.tar.gz \
  && tar -xf ktea-executable-server.tar.gz \
  && mv server /usr/local/bin/server \
  && chmod +x /usr/local/bin/server

ADD . .

FROM ubuntu

ARG RUBY_PATH=/usr/local
ARG RUBY_VERSION=2.6.3
ENV PATH $RUBY_PATH/bin:$PATH

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    gcc \
    make \
    libssl-dev \
    zlib1g-dev \
    build-essential \
    libreadline-dev

RUN git clone git://github.com/rbenv/ruby-build.git \
      $RUBY_PATH/plugins/ruby-build \
      &&  $RUBY_PATH/plugins/ruby-build/install.sh
RUN ruby-build $RUBY_VERSION $RUBY_PATH

RUN  wget -q https://github.com/nectar-cs/tam_server/releases/download/1.0.3/tam_server.tar.gz \
  && tar -xf tam_server.tar.gz \
  && mv tam_server /usr/local/bin/tam_server \
  && chmod +x /usr/local/bin/tam_server

WORKDIR /app
RUN gem install bundler -v 2.1.4
ADD local-eval.sh .
ENV TAM_CMD="/app/local-eval.sh"
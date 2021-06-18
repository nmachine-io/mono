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

RUN wget -q https://github.com/nmachine-io/ktea-executable-server/releases/download/1.0.8/ktea-executable-server.tar.gz \
  && tar -xf ktea-executable-server.tar.gz \
  && mv server /usr/local/bin/server \
  && chmod +x /usr/local/bin/server

WORKDIR /app
RUN gem install bundler -v 2.1.4
ADD local-eval.sh .
ENV KTEA_EXECUTABLE="/app/local-eval.sh"
FROM gcr.io/cloud-builders/gcloud

ARG RUBY_PATH=/usr/local
ARG RUBY_VERSION=2.6.3
ENV PATH $RUBY_PATH/bin:$PATH

RUN apt-get update && apt-get install -y git curl gcc make wget \
    libssl-dev zlib1g-dev build-essential libreadline-dev

RUN git clone git://github.com/rbenv/ruby-build.git \
      $RUBY_PATH/plugins/ruby-build \
      &&  $RUBY_PATH/plugins/ruby-build/install.sh
RUN ruby-build $RUBY_VERSION $RUBY_PATH

RUN gem install bundler -v 2.1.4

RUN mkdir /app
WORKDIR /app

ADD Gemfile Gemfile.lock /app/
RUN bundle update --bundler
RUN bundle
COPY . /app

ENTRYPOINT []
CMD ["/app/docker_cmd.sh"]

FROM ruby:2.6.3-alpine3.10
WORKDIR /app

# install packages and gems
RUN apk --update add build-base libxslt-dev libxml2-dev
ADD Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install

# add everything else
ADD . /app

# trickery for versions
ARG VERSION=none
RUN sed -i -e "s/version: none"/"version: $VERSION/g" values.yaml
RUN cat values.yaml

ENTRYPOINT ["bundle", "exec", "ruby", "/app/main.rb"]
FROM ruby:2.6.3-alpine3.10
WORKDIR /app

# install packages and gems
RUN apk --update add build-base libxslt-dev libxml2-dev
ADD Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install

# trickery for versions
ADD . /app
RUN rm values*
ARG VERSION
ADD values-$VERSION.yaml /app/values.yaml

ENTRYPOINT ["bundle", "exec", "ruby", "/app/main.rb"]
FROM ruby:2.6.3-alpine3.10
WORKDIR /app
RUN apk --update add build-base libxslt-dev libxml2-dev
ADD Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install
ADD . /app
ENTRYPOINT ["bundle", "exec", "ruby", "/app/main.rb"]
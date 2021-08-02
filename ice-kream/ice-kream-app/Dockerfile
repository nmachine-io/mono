FROM ruby:2.6.3

RUN apt-get update -qq && \
    apt-get install -y \
    nodejs postgresql-client

WORKDIR /app

ENV RAILS_ENV=production
ENV RACK_ENV=production

RUN gem install bundler:2.1.4
COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

RUN bundle exec rails SECRET_KEY_BASE=dummyvalue assets:precompile

EXPOSE 3000
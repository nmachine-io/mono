FROM us-central1-docker.pkg.dev/nectar-bazaar/public/kerbi2api:1.0.0
ADD Gemfile Gemfile.lock /app/
RUN bundle update --bundler
RUN bundle
ADD . .
CMD ["tam_server"]
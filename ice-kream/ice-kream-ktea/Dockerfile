FROM us-central1-docker.pkg.dev/nectar-bazaar/public/kerbi2api:1.0.1
ADD Gemfile Gemfile.lock /app/
RUN bundle update --bundler
ARG ICE_KREAM_VER
ENV ICE_KREAM_VER $ICE_KREAM_VER
RUN bundle
ADD . .
CMD ["server"]
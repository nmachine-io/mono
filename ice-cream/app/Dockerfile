FROM node:12
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8080
ARG VERSION
ENV FLAVOR="vanilla"
ENV VERSION=$VERSION
CMD [ "npm", "start" ]
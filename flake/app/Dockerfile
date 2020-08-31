FROM node:12
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8080
ENV FLAVOR="vanilla"
CMD [ "npm", "start" ]
FROM node:lts-alpine

ENV HOST=0.0.0.0

WORKDIR /home/app 

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
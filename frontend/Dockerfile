FROM node:lts-alpine

ENV HOST=0.0.0.0

WORKDIR /home/app 

COPY package.json .
COPY package-lock.json .

RUN npm install

RUN mkdir -p node_modules/.cache
RUN mkdir -p node_modules/.vite
RUN chmod -R 777 node_modules

COPY . .

CMD ["npm", "run", "dev"]
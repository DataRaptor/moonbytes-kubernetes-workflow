FROM node

EXPOSE 4203

WORKDIR /app

COPY . /app

RUN npm install 

RUN npm run build 

CMD ["npm", "run", "start"]


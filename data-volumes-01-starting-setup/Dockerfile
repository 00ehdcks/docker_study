FROM node:14



WORKDIR  /app

COPY package.json .

RUN npm install

COPY . .

#js에선 사용 불가능하고 도커파일 안에서만 사용가능하다.
ARG DEFAULT_PORT=80 

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

CMD [ "npm", "start" ]
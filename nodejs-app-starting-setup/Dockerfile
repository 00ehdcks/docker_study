FROM node:12

#작업공간
WORKDIR /app

#현재 폴더의 Dockerfile을 제외한 모든 파일을 /app으로 복사함
COPY package.json /app 

#npm을 설치
RUN npm install 

COPY . /app

#80port를 열어줌
#하지만 이미지 빌드후 런할때 포트를 추가로 인자로 지정해줘야함
#ex: docker run -p 3000:80 ID   >외부 3000포트와 도커80를 연결 localhost:3000으로 접속
EXPOSE 80

#컨테이너가 실행될때 실행됨. 'node server.js' 명령어를 띄어쓰기에 맞춰 2개의 인자로 전달
CMD [ "node", "server.js" ]
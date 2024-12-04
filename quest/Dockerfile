FROM node:16

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

ENV SECRET_WORD=We Did it!

EXPOSE 3000

CMD ["npm", "start"]
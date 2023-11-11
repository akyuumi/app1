# ビルドステージ
FROM node:18 AS build-stage
WORKDIR /app/fe
COPY ./package*.json ./
RUN npm install
COPY ./ ./
#RUN npm run build

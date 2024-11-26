FROM node:14 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve the application with a lightweight server
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

ARG ALPINE_VERION=3.20
FROM nginxinc/nginx-unprivileged:1.27-alpine${ALPINE_VERION}
USER 101
ADD nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /app
EXPOSE 8080
WORKDIR /app

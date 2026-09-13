FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY www /usr/share/nginx/html

EXPOSE 80 8443

CMD ["nginx", "-g", "daemon off;"]

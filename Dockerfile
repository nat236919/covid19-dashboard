FROM tiangolo/uwsgi-nginx-flask:python3.8
LABEL maintainer="Nuttaphat <nat236919@gmail.com>"

# setup uWSGI
ENV UWSGI_CHEAPER 4
ENV UWSGI_PROCESSES 64

# Set nginx
# https://github.com/tiangolo/uwsgi-nginx-flask-docker/issues/120
ENV NGINX_WORKER_PROCESSES auto
RUN echo "uwsgi_read_timeout 300s;" > /etc/nginx/conf.d/custom_timeout.conf

# Place your application on the server
WORKDIR /app
COPY ./app /app

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

EXPOSE 80/tcp
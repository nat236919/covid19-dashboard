FROM tiangolo/uwsgi-nginx:python3.8
LABEL maintainer="Nuttaphat <nat236919@gmail.com>"

# setup uWSGI
ENV UWSGI_CHEAPER 4
ENV UWSGI_PROCESSES 64

# Place your application on the server
WORKDIR /app
COPY ./app /app

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

EXPOSE 8080/tcp
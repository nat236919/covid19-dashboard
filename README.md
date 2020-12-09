<h1 align="center">
  COVID-19 DASHBOARD
</h1>

<p align="center">
    <em>Dashboard for exploring covid-19 cases around the globe powered by DASH framework</em>
</p>

<p align="center">
  <img src="https://i.ibb.co/YPPhKr3/dashboard-1.jpg">
</p>

# Introduction

**COVID-19 DASHBOARD** provides visualization from the COVID-19 data derived from [nat236919/covid19-api](https://github.com/nat236919/covid19-api). The core visualization framework relies heavily on [plotly/dash](https://github.com/plotly/dash) which offers swift and beautiful presentations.

## Installation (Docker-compose)

* Run the following command in your command line to run the server

```console
docker-compose up
```

* Or run the server in the background

```console
docker-compose up -d
```

* The port can be changed at <b>docker-compose.override.yml</b>

```yml
version: '3'
services:
  web:
    container_name: "covid19_dashboard_web_container"
    volumes:
      - ./app:/app
    ports:
      - "80:8080"
    command: python app.py
```

## Installation (from Dockerhub)

* Download the latest image

```console
docker pull nat236919/covid19-dashboard:latest
```

* Create a container and run

```console
docker run nat236919/covid19-dashboard
```

## Installation

* Install requirements

```console
pip install -r requirement.txt
```

* Run the following command in your command line to run the server

```console
python app.py
```

* Result

```console
Dash is running on http://127.0.0.1:8080/

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

## Visualization (Examples)

|  Chart Name           |     Graphic                                   |
| --------------------  | --------------------------------------------- |
| Chroleth              | <img src="https://i.ibb.co/FxRVzkr/g-1.jpg">  |
| Bubble                | <img src="https://i.ibb.co/Lkpb90q/g-2.jpg">  |
| Pie                   | <img src="https://i.ibb.co/r4SqpLv/g-3.jpg">  |
| Treemap               | <img src="https://i.ibb.co/WkCv1L9/g-4.jpg">  |

## Sponsor this project

<a href="https://www.buymeacoffee.com/HdYFLQU" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

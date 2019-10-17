# AirQuality

## Reason
The purpose of this project is learn how to build a webserver using django. 

## Objective
The objective of this project is to calculate the standard deviation with the given data that specifies the concentration of air pollutant
in the cities of China within the period from March 1st, 2013 to February 28th, 2017. The measures are used to gauge the air quality of each city.

## Beijing Multi-Site Air-Quality Data Data Set
Author: Dua, Dheeru and Graff, Casey.<br/>
Year: 2017<br/>
Title: Beijing Multi-Site Air-Quality Data Data Set<br/>
Url: https://archive.ics.uci.edu/ml/datasets/Beijing+Multi-Site+Air-Quality+Data#<br/>
Institution: University of California, Irvine, School of Information and Computer Sciences<br/>

## Build
Firstly you have to generate your own secret key and export it to an environment variable. 
To build the docker image and run it locally: 
```
docker build -t airquality:latest --build-arg SECRET_KEY=$SECRET_KEY . 
docker run -p 8000:8000 airquality:latest
```

## Deploy on Heroku
**Ensure that heroku is logged in<br/>
1. Create heroku app: <code>heroku create</code>
2. Add secret key to config vars: <code>heroku config:set SECRET_KEY=$SECRET_KEY</code> 
3. Build and push the docker image to heroku app: <code>heroku container: push web --app {APP NAME GENERATED}</code>
4. Deploy the pushed image: <code>heroku container:release web --app {APP NAME GENERATED}</code>


## Usage
There are three apps in this project.
##### List
To list all cities, add /cities/ at the end of url where a list of city will be presented in json format

##### Retrieve
To retrieve one specific city, add/cities/<pk> at the end of url where one city will presented in json format

##### get_std_dev action
Add /cities/<pk>/get_std_dev at the end of url, the standard deviation of each air pollutant in the city will be presented in json format.

## Technologies
Python 3.7<br/>
Django 2.2.6<br/>
Django Rest FrameWork 3.10.3<br/>
pandas 0.25.1<br/>
Gunicorn 19.9.0<br/>
Docker<br/>
Heroku<br/>

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

## How to Use
To use: export the secret key found in the key.txt in git bash. e.g. export SECRET_KEY='...' <br/>
To build the docker image: docker build -t airquality:latest --build-arg SECRET_KEY = $SECRET_KEY . <br/>
To run the docker locally: docker run -p portnumber airquality:latest<br/>

## Deply on Heroku
**Esnure that heroku is logged in<br/>
To create heroku app: heroku create<br/>
To push docker file to app: heroku container: push web --app {APP NAME GENERATED}<br/> 
To open web app: heroku open --app {APP NAME GENERATED}<br/>


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
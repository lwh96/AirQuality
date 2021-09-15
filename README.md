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
1. Create heroku app: `heroku create`
2. Add secret key to config vars: `heroku config:set SECRET_KEY=$SECRET_KEY`
3. Build and push the docker image to heroku app: `heroku container: push web --app {APP NAME GENERATED}`
4. Deploy the pushed image: `heroku container:release web --app {APP NAME GENERATED}`


## Usage
There are three apps in this project.
##### List
To list all cities: `GET /city`

##### Retrieve
To retrieve one specific city: `GET /city/<pk>` <br/>
where pk is the primary key ranging from 1 to 12

##### get_std_dev action
To perform the compute action on specified city: `GET /city/<pk>/get_std_dev`<br/> 
where pk is the primary key ranging from 1 to 12

## Technologies
Python 3.7<br/>
Django 2.2.6<br/>
Django Rest FrameWork 3.10.3<br/>
pandas 0.25.1<br/>
Gunicorn 19.9.0<br/>
Docker<br/>
Heroku<br/>

<table width="100%">
    <tr><td colspan=5><b>Group Name:  PROJ - Project Information
<b></th></td>
    <tr>
        <th>Status</th>
        <th>Heading</th>
        <th colspan=2 >SuggestedUnit/Type</th>
        <th>Description</th>
        <th>Exampple</th>
    </tr>
    <tr>
        <td>*R</td>
        <td>PROJ_ID</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">ID</td>
        <td>Project identifier</td>
        <td>121415</td>
    </tr>
    <tr>
        <td></td>
        <td>PROJ_NAME</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">X</td>
        <td>Project Title</td>
        <td>ACME Gas Works Redevelopment</td>
    </tr>
    <tr>
        <td>R</td>
        <td>PROJ_LOC</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">X</td>
        <td>Location of site</td>
        <td>High Street, Anytown</td>
    </tr>
    <tr>
        <td></td>
        <td>PROJ_CLNT</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">X</td>
        <td>Client Nam</td>
        <td>ACME Enterprises</td>
    </tr>
    <tr>
        <td></td>
        <td>PROJ_CONT</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">X</td>
        <td>Contractor Name</td>
        <td>ACME Drilling Ltd</td>
    </tr>
    <tr>
        <td></td>
        <td>PROJ_ENG</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">X</td>
        <td>Project Engineer</td>
        <td>ACME Consulting</td>
    </tr>
    <tr>
        <td></td>
        <td>PROJ_MEMO</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">X</td>
        <td>General project comments</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>FILE_SET</td>
        <td style="text-align:center;"></td>
        <td style="text-align:center;">X</td>
        <td width="1">Associated file reference (e.g. project specification, site location drawings)</td>
        <td>FS1</td>
    </tr>
</table>

###### Group Notes
* PROJ is required in all AGS4 files (Rule 13).
* PROJ_ENG should contain the details of the consultant/designer for the project.


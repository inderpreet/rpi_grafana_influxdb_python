# Grafana and InfluxDB Dashboard with Raspberry pi

This repository contains docker and python files for a dashboard implementation using gGrafana and InfluxDB. If you are looking for the x86 version of the same project, please take a look at [https://github.com/inderpreet/py_docker_grafana_influxdb_dashboard](https://github.com/inderpreet/py_docker_grafana_influxdb_dashboard).

For more information visit [hackaday - 
Howto: Docker, Databases, and Dashboards to Deal with Your Data](https://hackaday.com/2019/01/23/howto-docker-databases-and-dashboards-to-deal-with-your-data/)

## Pre-requisites

Make sure you have docker, docker-compose, python, pip and virtualenv installed. At the time of this writing, the test Raspberry Pi 3 was using

- Docker version 18.09.0, build 4d60db4
- Python 2.7.13

To install docker on the Raspberry Pi, run the following command at the prompt

```bash
curl -sSL https://get.docker.com |sh
sudo apt-get update && sudo apt-get install docker-compose virtualenv
```

I am assuming that python comes preinstalled.

In addition to the Raspberry Pi 2 or 3, you will need a Sense-Hat. You MAY use some other sensor or dummy data for testing.

## Usage

This repository was written for the article at [hackaday - 
Howto: Docker, Databases, and Dashboards to Deal with Your Data](https://hackaday.com/2019/01/23/howto-docker-databases-and-dashboards-to-deal-with-your-data/)

The following simple steps should get you up and running quickly.

### Clone the Repo

Clone the repository by running 

```bash
git clone https://github.com/inderpreet/rpi_grafana_influxdb_python
```

### Begin the Docker container

The docker-compose.yml contains details about two application containers- InfluxDB and Grafana. The versions and some other details are part of the script and all you have to do is run

```bash
docker-compose up -d
```

### Logging In and Connecting Grafana and InfluxDB

Grafana should be up and running and you can use your favourite browser to connect to http://raspberry-pi:3000  or use the IP address of the Pi with port number 3000. Use username Admin and Password Admin to open up the dashboard. To add an Influx connection, you can run the command

```
./add_datasource.sh
```

Once you refresh the browser, the influx should be setup. Cool!

### Pushing Temperature data from the Sense-Hat

For testing you may run 

```
pip install -r ./pyclient/requirements.txt
python ./pyclient/test.py 
```

This will generate an exponential data stream and push to the influxDB. To use the Sense-Hat, replace the test.py in the above command with sense_hat_temperature.py 

For more details visit the hackaday link provided above.

## Author and License

Designed by [Inderpreet Singh](https://inderpreet.github.io)

This software may be distributed and modified under the terms of the GNU
General Public License version 2 (GPL2) as published by the Free Software
Foundation and appearing in the file LICENSE.TXT included in the packaging of
this file. Please note that GPL2 Section 2[b] requires that all works based
on this software must also be made publicly available under the terms of
the GPL2 ("Copyleft").

We put a lot of time and effort into our project and hence this copyright 
notice ensures that people contribute as well as each contribution is 
acknowledged. Please retain this original notice and if you make changes
please document them below along with your details.

The latest copy of this project/library can be found at: 
https://github.com/inderpreet/

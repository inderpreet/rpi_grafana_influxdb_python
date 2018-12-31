#!/bin/sh
# Run this script after the docker containers are running to add the datasource to the Grafana Soruces
curl --header "Content-Type: application/json" -vX POST http://admin:admin@127.0.0.1:3000/api/datasources -d @influx.json

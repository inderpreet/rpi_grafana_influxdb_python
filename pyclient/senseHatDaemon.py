#!/usr/bin/env python

import sys, time
from influxdb import InfluxDBClient
import time
from sense_hat import SenseHat
from daemon import Daemon

sense = SenseHat()

class senseHatDaemon(Daemon):
	def run(self):
		humidity = 1.1
		temperature = 1.1	    
		while(True):
			
			humidity = sense.get_humidity()
			temperature = sense.get_temperature()
			json_body = [
				{
					"measurement": "sensorData",
					"tags": {
						"source": "Raspberry Pi",
						"type": "sense hat"
					},
					"fields": {
						"temperature": temperature,
						"humidity": humidity
					}
				}
			]
			client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'hackaday')
			client.create_database('hackaday')
			client.write_points(json_body)
			result = client.query('select value from sensorData;')
			print("Result: {0}".format(result))
			time.sleep(60)
 

if __name__ == "__main__":
	daemon = senseHatDaemon('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)

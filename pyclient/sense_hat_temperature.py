from influxdb import InfluxDBClient
import time
from sense_hat import SenseHat

sense = SenseHat()


if __name__ == "__main__":
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
 

from influxdb import InfluxDBClient
import time



if __name__ == "__main__":
    i=1.1
    while(True):
        json_body = [
            {
                "measurement": "sensorData",
                "tags": {
                    "source": "bedroom",
                    "type": "temperature"
                },
                "fields": {
                    "value": i
                }
            }
        ]

        i=i*1.1
        if(i >= 100.0):
            i=1.1
        client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'hackaday')

        client.create_database('hackaday')

        client.write_points(json_body)

        result = client.query('select value from sensorData;')

        print("Result: {0}".format(result))

        time.sleep(1)
        
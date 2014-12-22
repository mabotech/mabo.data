# -*- coding: utf-8 -*-

""" influxdb points generator """

import time


from influxdb import client as influxdb


class InfluxDB(object):
    
    def __init__(self):
        """ initial db connection """
        
        self.db = influxdb.InfluxDBClient("192.168.100.112", "8086", "root","root","monitor")


    
    def gen(self):
        """ generate data """
        
        timestamp_now = time.time()
        timestamp2 = timestamp_now+10

        json_body = [
          {
            "points": [
                [timestamp_now, "1", 11, 31.0],
                [timestamp2, "2", 21, 21.0]
            ],
            "name": "t2",
            "columns": ["time", "c", "a", "b"]
          }
        ]

        """
        result = self.db.query('select count(a) from t2;')

        print (result)
        """
        self.db.write_points(json_body)


def main():
    
    influx = InfluxDB()

    influx.gen()


if __name__ == "__main__":
    main()

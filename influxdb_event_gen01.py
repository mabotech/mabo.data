# -*- coding: utf-8 -*-

""" influxdb points generator """

import time

import random

import socket

import gevent

from influxdb import client as influxdb


class InfluxDB(object):
    
    def __init__(self, host, port, username, password, database):
        """ initial db connection """
        
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        
        self.db = influxdb.InfluxDBClient(self.host, self.port, self.username, self.password, self.database)

    def reconnect(self):
        """ reconnect """
        
        print("reconnect")
        self.db = influxdb.InfluxDBClient(self.host, self.port, self.username, self.password, self.database)
    
    def gen(self):
        """ generate data """
        
        timestamp_now = time.time() #-8*60*60
        
        val_a = "tags:%s" %(random.randint(1, 100) )
        val_b = "text-%s" %(random.randint(1, 100) )
        val_c = "title-%s" %(random.randint(1, 100) )
        
        print(timestamp_now, val_a, val_c, val_c)
        #timestamp2 = timestamp_now+10

        json_body = [
          {
            "points": [
                [timestamp_now, val_a,val_b,val_c]             
            ],
            "name": "events",
            "columns": ["time", "tags","text","title"]
          }
        ]

        """
        result = self.db.query('select count(a) from t2;')

        print (result)
        """
        print (json_body)
        v = self.db.write_points(json_body)
        print v


def main(sleep_seconds):
    """ main """
    
    influx = InfluxDB("192.168.147.140", "8086", "root","root","monitor")
    
    while True:
        try:
            influx.gen()
            gevent.sleep(sleep_seconds)
        #except ConnectionError as cerr:
        #    influx.reconnect()
        #    raise(Exception("err"))
        except Exception as exc:
            print(exc)
            raise(Exception("err"))
        
if __name__ == "__main__":
    sleep_seconds = 10
    main(sleep_seconds)

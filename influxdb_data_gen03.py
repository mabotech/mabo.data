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
        
        val_a = random.randint(1, 4)
        val_b = random.randint(1, 4)
        val_c = random.randint(1, 4)
        val_d = random.randint(1, 4)
        val_e = random.randint(1, 4)
        val_f = random.randint(1, 4)
        val_g = random.randint(1, 4)
        val_h = random.randint(1, 4)
        val_i = random.randint(1, 4)
        val_j = random.randint(1, 4)         
        
        print(timestamp_now, val_a, val_c, val_c)
        #timestamp2 = timestamp_now+10

        json_body = [
          {
            "points": [
                [timestamp_now, val_a,val_b,val_c,val_d,val_e,val_f,val_g, val_h,val_i,val_j]             
            ],
            "name": "st",
            "columns": ["time", "a","b","c","d","e","f","g","h","i","j"]
          }
        ]

        """
        result = self.db.query('select count(a) from t2;')

        print (result)
        """
        print (json_body)
        self.db.write_points(json_body)


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

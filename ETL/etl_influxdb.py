# -*- coding: utf-8 -*-


from influxdb import InfluxDBClient

import logbook

logger = logbook.Logger(__name__)


class InfluxETL(object):
    """ influxdb lib """
    def __init__(self, config):
        """ init """
        
        logger.debug("init...")
        #self.client = InfluxDBClient('localhost', 8086, 'root', 'root', 'mabo')
        self.config = config["influxdb"]
        self.connect()
        
        self.measurement = self.config['measurement']
        self.last_id = self.config['last_id']
        
    def connect(self):
        """ connect influxdb """
        
        self.client = InfluxDBClient(self.config['host'], 
            self.config['port'], self.config['user'], 
            self.config['password'], self.config['db'])
            
    def write_points(self, json_body):
        """ write point """
        
        self.client.write_points(json_body)
        
        
    def write_data(self, timestamp, running, idle, fail):
        """ write """
        
        json_body = [
            {
                "measurement": self.measurement,
                "time": timestamp,
                "fields":{
                    "running": running,
                    "idle": idle,
                    "fail": fail
                }
            }
        ]

        self.write_points(json_body)
        
    def write_last_id(self, pkey):
        """ update last id(pg pkey) """
        
        #t = time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime())       
        
        json_body = [
            {
                "measurement": self.last_id,
                "time": self.config['timestamp'],
                "fields":{
                    "pkey": pkey,
                }
            }
        ]

        self.write_points(json_body)
        
    def get_last_inserted(self):
        """ get last inserted id """        
              
        #print v.raw
        try:
            v = self.client.query('select pkey from %s' %(self.last_id))  
            pkey = v.raw['series'][0]['values'][0][1]
        except Exception as ex:
            #print ex.message
            pkey = None
        return pkey
           
def test():
    """ test """
    import toml

    with open("config.toml") as conf_file:
        config = toml.loads(conf_file.read())
    
    db = BizInflux(config)
    #db.write_last_id(63620)
    print db.get_last_inserted()
    
if __name__ == "__main__":
    test()        
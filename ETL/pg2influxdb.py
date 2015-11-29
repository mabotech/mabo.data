# -*- coding: utf-8 -*-

"""
TODO: 
- heartbeat
- logging

https://pythonhosted.org/psycopg2/advanced.html#asynchronous-notifications
Psycopg allows asynchronous interaction with **other database sessions**

"""
#
#import gevent.monkey

#gevent.monkey.patch_all()



#import select


import datetime

import time
from time import strftime, localtime

#import gevent


import logbook

import toml

with open("config.toml") as conf_file:
    config = toml.loads(conf_file.read())

logconf = config["logging"]

logbook.set_datetime_format("local")

logger = logbook.Logger('pg2influx')

#log = logbook.FileHandler('heka_tcp.log')

log = logbook.RotatingFileHandler(logconf['logfile'], \
        max_size=logconf['max_size'], \
        backup_count=logconf['backup_count'], \
        level = logconf['level'], \
        bubble=True)

log.format_string = logconf['format_string']


log.default_format_string = logconf['default_format_string']

log.push_application()


from utils import heartbeat

from etl_pg import PgETL
from etl_influxdb import InfluxETL

# configuration

    
def run():
    """ run """  
    
    logger.debug("run...")

    db = InfluxETL(config)
    pg = PgETL(config)
    
    last_inserted = db.get_last_inserted()        
    #print last_inserted    
    #return 1
    
    if last_inserted == None:    
        row_id = pg.get_min()
    else:
        row_id = last_inserted
    
    last_db_id = pg.get_max()
    
    #print "last:%s" %(last_db_id)
    
    # loop with dynamic sleep time
    
    while 1:
    
        #for row_id in xrange(begin, end+1):       
        #print row_id
        
        heartbeat("pg2influxdb")
        
        row = pg.get_data(row_id)
        
        if row == None:
            #print row_id
            if row_id <= last_db_id:
                row_id = row_id + 1
            else:
                
                last_id = pg.get_max()
                
                if last_id == last_db_id:
                    #print (time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime()))             
                    
                    ltime = time.localtime()
                    tm_wday = ltime.tm_wday
                    tm_hour = ltime.tm_hour
                    
                    if tm_wday in (5,6) or tm_hour < 8 or tm_hour > 18:
                        # rest time
                        sleeptime = 60
                    else:     
                        # working time
                        sleeptime = 6                   
                    
                    time.sleep(sleeptime)                  
                    
                else:
                    last_db_id = last_id
            
            continue
        
        timestamp = "%s+08:00" %(row[1].isoformat())
        
        # timezone: +08:00
        #UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%f+08:00"
        #print datetime.datetime.strptime(row[1],UTC_FORMAT)
        #print(timestamp+"Z")
        #print("%s,%s,%s" %(row[2],row[3],row[4]))        
        #print("%s"%(row_id))        
        
        db.write_data(timestamp,row[2],row[3],row[4] )
        db.write_last_id(row_id)
        
        row_id = row_id + 1        
        #time.sleep(0.01)


def main():
    """ main """
    
    run()
    
if __name__ == "__main__":
    main()

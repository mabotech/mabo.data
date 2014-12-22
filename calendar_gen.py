# -*- coding: utf-8 -*-

import time
import calendar

import arrow
#import datetime

def get_day(year, month):
    """ yield month days """
    
    firstweekday = 0

    monthdays = calendar.Calendar(firstweekday).itermonthdays2(year, month)    

    for day in monthdays:
        if day[0] > 0:
            date =  "%d-%02d-%02d" % (year, month, day[0])            
            timestamp =  time.mktime((year, month, day[0], 0, 0, 0, day[1], 0, 0))            
            weekday =  day[1]
            yield (date, timestamp, weekday)
            
def get_day2(year, month):
    """ yield month days """
    
    firstweekday = 0
    monthdays = calendar.Calendar(firstweekday).itermonthdays2(year, month)
    for day in monthdays:
        if day[0] > 0:
            
            ds = '%d-%02d-%02dT00:00:00.000000+08:00' % (year, month, day[0])
            date = arrow.get(ds)            
            #print date.format('YYYY-MM-DD HH:mm:ss ZZ')           
            timestamp =  time.mktime((year, month, day[0], 0, 0, 0, day[1], 0, 0))            
            weekday =  day[1]
            yield (date, date.timestamp, weekday)            

def main(from_year, to_year):
    
    for year in range(from_year, to_year):
            
        for month in range(1, 13):
      
            for day_info in get_day2(year, month):
                print "%s,%d,%s" %(day_info[0], 1000*day_info[1], day_info[2]+1)
                sql =  "insert into calendar (_date, weekday) values('%s','%s')" %(day_info[0], day_info[1])                
                #print(sql)
                
            
if __name__ == "__main__":
    
    main(2014, 2015)
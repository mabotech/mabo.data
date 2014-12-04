# -*- coding: utf-8 -*-

import calendar
#import datetime

def days(year, month):
    """ yield month days """
    
    firstweekday = 0

    monthdays = calendar.Calendar(firstweekday).itermonthdays2(year, month)    

    for day in monthdays:
        
        if day[0] > 0:
        
            date =  "%s-%s-%s"%(year, month, day[0])
            weekday =  day[1]+1
            yield (date, weekday)
            

def main(from_year, to_year):
    
    for year in range(from_year, to_year):
            
        for month in range(1, 13):
      
            for day in days(year, month):
                
                sql =  "insert into calendar (_date, weekday) values('%s','%s')" %(day[0], day[1])
                
                print(sql)
                
            
if __name__ == "__main__":
    
    main(2014, 2015)
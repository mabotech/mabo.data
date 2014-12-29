# -*- coding: utf-8 -*-


import calendar

import random

def main(year, month):
    
    #print dir(random)
    monthdays = calendar.Calendar(0).itermonthdays2(year, month) 
    
    i = 0
    for day in monthdays:
        if day[0]>0:
            if day[1] in [5,6]:
                v1 = v2 = 0
            else:
                v1 = random.randint(40,100)
                v2 = random.randint(40,100)
            i = i +1
            print "%s    %s-%s-%s    %s    %s    %s" %(i, year, month, day[0], day[1], v1, v2)

def downtime():
    
    
    for eq in range(1, 8):
        v1 = random.randint(0,40)
        v2 = random.randint(40,100)
        print "%s    %s%s    %s    %s    %s" %(eq, "设备", eq, v1/20.0, v2/20.0, abs(2-v2/20))
        
if __name__ == "__main__":
    #main(2014, 12)
    
    downtime()
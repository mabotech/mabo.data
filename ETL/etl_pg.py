# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extensions

import logbook

logger = logbook.Logger(__name__)

class PgETL(object):
    """ PostgreSQL Lib """
    
    def __init__(self, config):
        """ init """
        logger.debug("init...")
        
        self.config = config['postgresql']
        
        self.table = "buss_equipstatussumm"
        self.connect()
        
    def connect(self):
        """ connect """
        
        DSN = self.config['DSN']        
        
        conn = psycopg2.connect(DSN)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        
        self.curs = conn.cursor()         
    
    def fetchone(self, sql):
        """ fetchone """
        
        self.curs.execute(sql)
        row = self.curs.fetchone()
        
        return row
        
    def get_min(self):
        """ get min pkey """
        
        sql = """select min(id) from %s""" %(self.table)
        row = self.fetchone(sql)
        
        return row[0]        
        
    def get_max(self):
        """ get max pkey """
        
        sql = """select max(id) from %s""" %(self.table)
        row = self.fetchone(sql)
        
        return row[0]
        
    def get_data(self, pkey):    
        """ get record by pkey """
        
        sql = """select * from buss_equipstatussumm where id = %s""" %(pkey)
        row = self.fetchone(sql)
    
        return row
   
def test():
    import toml

    with open("config.toml") as conf_file:
        config = toml.loads(conf_file.read())
        
    db = PgETL(config)
    
    print(db.get_max())
    
if __name__ == "__main__":
    test()
    
    
# -*- coding: utf-8 -*-

import logbook

logger = logbook.Logger(__name__)

def heartbeat(name):
    """ heartbeat declare """
    logger.debug("hb")
    pass
    
def test():
    pass
    
if __name__ == "__main__":
    test()    
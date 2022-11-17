import logging

def get_logger(name):
    co_logger = logging.getLogger(name)
    handler = logging.FileHandler('./log/'+cal_std_day(0)+'.log')
    co_logger.addHandler(handler)
    return co_logger
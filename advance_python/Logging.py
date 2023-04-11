#Visit website for revision
#https://github.com/patrickloeber/python-engineer-notebooks/blob/master/advanced-python/10-Logging.ipynb

import logging

#logging level: debug, info, warning, error, critical

# logging.info("information")
# logging.debug("debug")
# logging.warning('warning')
# logging.error("error")
# logging.critical("critical")
#Bydefault only critical, warning and error are printed but we can configure for debug and info. Comment the above and then run below

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - $(levelname)s - %(message)s',
#                     datefmt="%m/%d/%Y %H:%M:%S")
#
# logging.info("information")
# logging.debug("debug")
# logging.warning('warning')
# logging.error("error")
# logging.critical("critical")

#its not a good practise to use root logger instead we will create our own logger with helper.py
#comment all the above before making use of the below

# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt="%m/%d/%Y %H:%M:%S")
# import helper



import logging



# #create logger
# logger = logging.getLogger(__name__)
#
# #create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')
#
# #set log level and format for each handler
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)
#
# #set format for each handler
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)
#
# #add handler to the logger
# logger.addHandler(stream_h)
# logger.addHandler(file_h)
#
# logger.warning('this is a warning')
# logger.error('this is a error')




#Logging with config file

# import logging.config
#
# logging.config.fileConfig('logging.conf')
#
# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug')


import logging
# try:
#     a =[1,2,3]
#     val = a[4]
# except IndexError as e:
#     # logging.error(e)
#     #if you want to enable stack trace with logger
#     logging.error(e, exc_info=True)

#lets say we don't know the error type and still we want to stack trace then

# import logging
# import traceback
# try:
#     a =[1,2,3]
#     val = a[4]
# except:
#     logging.error(f'The error is {traceback.format_exc()}')


#Rotating file handler
# import logging
# from logging.handlers import RotatingFileHandler
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# # roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)
#
#
# for _ in range(10000):
#     logger.info('Hello, world!')


#TimeRotatingFilehandler
import logging
import time
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for i in range(6):
    logger.info('Hello, world!')
    time.sleep(5)
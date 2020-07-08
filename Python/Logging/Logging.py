import logging

logging.basicConfig(level=logging.DEBUG) # Tells it at what level to
# start displaying the messages

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is an warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

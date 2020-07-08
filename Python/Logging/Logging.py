import logging

# logging.basicConfig(level=logging.DEBUG) # Tells it at what level to
# start displaying the messages
                                        # w = write mode                            # %(name)s - (displays 'root')
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is an warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
name = 'bob'
logging.error('%s raised an error', name)

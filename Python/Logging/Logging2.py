import logging

logging.basicConfig(level=logging.INFO, filename='moj.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M')

name= 'bob'
logging.info('%s - Resolved as invalid', name)

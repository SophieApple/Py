import logging

logging.basicConfig(filename='test.log',filemode='a',format="%(asctime)s %(name)s:%(levelname)s:%(message)s",datefmt="%d-%M-%Y %H:%M:%S",level=logging.DEBUG)
try:
    a = 'a'
except Exception as e:
    logging.exception(e)
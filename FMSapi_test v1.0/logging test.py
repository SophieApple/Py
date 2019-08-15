import configparser

cf = configparser.ConfigParser()
cf.read('./config.ini')

secs = cf.sections()
print(secs)
print(secs[0][1])
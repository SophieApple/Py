import configparser

cf = configparser.ConfigParser()
cf.read('./profile.ini')
secs = cf.sections()

print(secs)

options = cf.options('config')
print(options)

items = cf.items('config')
print(items)


host = cf.get('config','order_id')
print(host)
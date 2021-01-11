from Properties import Properties
properties = Properties("my.properties")

price = float(properties.get_single_property('price'))

print('price: ' + str(price))

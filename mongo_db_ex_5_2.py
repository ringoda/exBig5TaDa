from pymongo import MongoClient

#Connect to Mongo which is running on localhost:27017
client = MongoClient('localhost', 27017)

#Get the database
db = client.Northwind

#Lists we will use to gather data
alfkis_orders = []
alfkis_productid = []

#Find and collect 'ALFKI' orders
for orderIDs in db.orders.find({'CustomerID': 'ALFKI'}):
	alfkis_orders.append(orderIDs['OrderID'])

#Find and collect 'ALFKI' products from his orderIDs
for orderid in alfkis_orders:
	#First we check how many different products are in his order and disregard it if it's less than 2
	if db['order-details'].find({'OrderID': orderid}).count() >= 2:
		for productids in db['order-details'].find({'OrderID': orderid}):
			alfkis_productid.append((orderid, productids['ProductID']))

print "Order ID\tProduct ID\tProduct Name"
print "============================================"

#Find and print the productName of 'ALFKI' orders along with productID and orderID
for products in alfkis_productid:
	print str(products[0]) + '\t\t' + str(products[1]) + '\t\t' + db.products.find_one({'ProductID': products[1]})['ProductName']

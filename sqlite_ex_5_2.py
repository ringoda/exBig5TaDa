import sqlite3

#Connect to our database
conn = sqlite3.connect('northwind.db')

#This was needed to decode a product name
conn.text_factory = str

#Get a cursor object in the database
c = conn.cursor()

#The CustomerID we are looking for
customer = u'ALFKI'

#List we will use to gather relevant data
list_of_orderIDs = []
list_of_productIDs = []
tmp_list_of_orders = []

#Get all orderIDs for our customer
for order_id in c.execute('SELECT OrderID FROM Orders WHERE CustomerID=:id', {"id": customer}):
	tmp_list_of_orders.append(order_id[0])

#Lets count the number of different products each order contains, we use COUNT() for that
for order in tmp_list_of_orders:
	for count_products in c.execute('SELECT COUNT(ProductID) FROM "Order Details" WHERE OrderID=:id', {"id": order}):
		#If the order has 2 or more different products we add it to out list of orderIDs
		if count_products[0] >= 2:
			list_of_orderIDs.append(order)	

#Loop through the orderIDs and get the productIDs
for order in list_of_orderIDs:
	for product_id in c.execute('SELECT ProductID FROM "Order Details" WHERE OrderID=:id', {"id": order}):
		list_of_productIDs.append((order, product_id[0]))

print "Order ID\tProduct ID\tProduct Name"
print "============================================"

for products in list_of_productIDs:
	#Find and print the productName along with productID and orderID
	for product in c.execute('SELECT ProductName FROM "Products" WHERE ProductID=:id', {"id": products[1]}): 
		print str(products[0]) + '\t\t' + str(products[1]) + '\t\t' + product[0]




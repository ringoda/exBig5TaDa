import sqlite3

conn = sqlite3.connect('northwind.db')

conn.text_factory = str

c = conn.cursor()

customer = u'ALFKI'

print "Order ID\tProduct ID\tProduct Name"
print "============================================"

for results in c.execute("""SELECT COUNT(DISTINCT o.OrderID)
							 FROM "Order Details" od
							 inner join Orders o
							 	on o.OrderID =  od.OrderID
							 inner join Products p
							 	on p.ProductID = od.ProductID
							 WHERE o.CustomerID=:id""", {"id": customer}):

	print results
	#print str(results[0]) + '\t\t' + str(results[2]) + '\t\t' + results[1]

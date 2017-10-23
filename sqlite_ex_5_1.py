import sqlite3

#Connect to our database
conn = sqlite3.connect('northwind.db')

#This was needed to decode a product name
conn.text_factory = str

#Get a cursor object in the database
c = conn.cursor()

#The CustomerID we are looking for
customer = u'ALFKI'

print "Order ID\tProduct ID\tProduct Name"
print "============================================"

#Now we execute the query and loop through the results
#We join the three tables we are interested in and 
# get the relevant information for our customer
for results in c.execute("""SELECT o.OrderID, p.ProductName,p.ProductID  
							 FROM "Order Details" od
							 inner join Orders o
							 	on o.OrderID =  od.OrderID
							 inner join Products p
							 	on p.ProductID = od.ProductID
							 WHERE o.CustomerID=:id""", {"id": customer}):
	#print the result
	print str(results[0]) + '\t\t' + str(results[2]) + '\t\t' + results[1]

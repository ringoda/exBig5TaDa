import sqlite3

#Connect to our database
conn = sqlite3.connect('northwind.db')

#This was needed to decode a product name
conn.text_factory = str

#Get a cursor object in the database
c = conn.cursor()


list_of_employers = []

#Get all employeeIDs
for emp in c.execute('SELECT EmployeeID FROM Employees'):
	list_of_employers.append(emp[0])

print "Nr. Of Orders\tFirst Name\tLast Name"
print "============================================"

#Now we execute the query and loop through the results
#We join the two tables we are interested in and 
# get the relevant information for our employees and use COUNT()
# to get the number of orders for each
for employee in list_of_employers:
	for results in c.execute("""SELECT COUNT(e.EmployeeID), e.FirstName, e.LastName, 
								 FROM Employees e
								 inner join Orders o
								 	on o.EmployeeID =  e.EmployeeID
								 WHERE e.EmployeeID=:id""", {'id':employee}):
		#print the result
		print str(results[0]) + '\t\t' + str(results[1]) + '\t\t' + str(results[2])

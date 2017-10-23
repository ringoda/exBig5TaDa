from pymongo import MongoClient

#Connect to Mongo which is running on localhost:27017
client = MongoClient('localhost', 27017)

#Get the database
db = client.Northwind

#List we will use to gather data
list_of_employees = []

#Find and collect all employee IDs
for employee in db.employees.find():
	list_of_employees.append(employee['EmployeeID'])

print "Nr. Of Orders\tFirst Name\tLast Name"
print "============================================"

#Find and collect 'ALFKI' products from his orderIDs
for employeeid in list_of_employees:
	#Get the employee information
	employee = db.employees.find_one({'EmployeeID': employeeid})
	#Count number of orders and
	count = db.orders.find({'EmployeeID': employeeid}).count()
	if count > 0:
		#Print number of orders and the first and last name of the employee
		print str(count) + '\t\t' + employee['FirstName'] + '\t\t' + employee['LastName']
	


import csv

salesFile = open('sales-demo.csv')

salesDict = csv.DictReader(salesFile)

# for line in salesFile.readlines():
#     lines = line.split(",")
#     print(lines)

canceledOrders = []

for line in salesDict:
    if line['Status'].upper() == 'CANCELLED':
        canceledOrders.append(line)

#print(canceledOrders)

# for line in canceledOrders:
#     print(line)

# total = 0.0

# for line in canceledOrders:
#     total += float(line['Total'])

# print(total)

customerlist = []
for line in salesDict:
    if line['Customer_Name'].lower() in ['mohammed','ramesh']:
        customerlist.append(line)

print(customerlist)

customFile = open("customFile.csv" , "w")

fields = ["Invoice","Customer_Name","Product Name","Qty","Rate","Status","Total"]

writer = csv.DictWriter(customFile,fieldnames=fields)
writer.writeheader()

#writer.writerows(customerlist)
for line in customerlist:
    value = {
        'Customer_Name':line['Customer_Name'],
        'Total':line['Total']
    }
    writer.writerow(value)
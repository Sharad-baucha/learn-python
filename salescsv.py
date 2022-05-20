   
import csv
sales_file = open('./sales-demo.csv')

sales_dict = csv.DictReader(sales_file)  # Creates a list of dictionaries.

cancelledOrders = []

total_of_cancelled_orders = 0.0

# for line in sales_dict:
#     # lines = line.split(",")
#     print(line)

for line in sales_dict:
    # lines = line.split(",")
    # print(lines)

    if line['Status'].upper() == 'CANCELLED':
        cancelledOrders.append(line)

#print(cancelledOrders)


# Computing the total of cancelled orders

# for line in cancelledOrders:
#     print(type(line))
#     total_of_cancelled_orders += float(line['Total'])

# print("Total = ", total_of_cancelled_orders)


# Filtering the data values based on the name of the customer .(name must be 'mohammed' or 'Ramesh')

filtered_list = []

# for names in sales_dict:
#     if names['Customer_Name'].title() == 'Mohammed' or names['Customer_Name'].title() == 'Ramesh':
#         filtered_list.append(names)
# print(filtered_list)


# Version 2 of the method.

# for line in sales_dict:
#     if line['Customer_Name'].title() in ['Mohammed', 'Ramesh']:
#         filtered_list.append(line)

# print(filtered_list)

# Filtered Customer file

customer_file = open('customname.csv', 'w')

# fields = ['Invoice_ID', 'Customer_Name',
#   'Product Name', 'Qty', 'Rate', 'Status', 'Total']

# Field names are for filtering the data
fields = ['Customer_Name', 'Total']
writer = csv.DictWriter(customer_file, fieldnames=fields)

# For Writing the headers
writer.writeheader()

# writer.writerows(filtered_list)

# File Modes
# 'x' -> For creating file for logrotate purpose.


# For writing the selected filednames in the file.


# for line in filtered_list:
#     value = {
#         'Customer_Name': line['Customer_Name'],
#         'Total': line['Total']
#     }
#     writer.writerow(value)

# customer_file.close()

approvedorders = []

for line in sales_dict:
    if line['Status'].upper() == 'APPROVED':
        a = {
            'Customer_Name': line['Customer_Name'],
            'Product Name': line['Product Name'],
            'Qty': line['Qty']
        }
        approvedorders.append(a)

# for line in approvedorders:
#     print(line)

topproduct = {}

for line in approvedorders:
    Product_Name = line['Product Name']
    if Product_Name in topproduct:
        topproduct[Product_Name] += int(line['Qty'])
    else:
        topproduct[Product_Name] = int(line['Qty'])
        
# for line in topproduct:
#     print(line)
#print(topproduct)

#print(topproduct.values())

max = 0
for key , value in topproduct.items():
    if value > max:
        max = value
        Product = key

#print(Product,max)

sorted_product = {key: value for key, value in sorted(topproduct.items(),reverse=True, key=lambda item: item[1])}

#print(sorted_product)

topcustomer = {}
order = []
for line in approvedorders:
    Customer_Name = line['Customer_Name']
    if Customer_Name in topcustomer:
        topcustomer[Customer_Name] += int(line['Qty'])
    else:
        topcustomer[Customer_Name] = int(line['Qty'])

#print(topcustomer)
sorted_customer = {key: value for key, value in sorted(topcustomer.items(),reverse=True, key=lambda item: item[1])}
#print(sorted_customer)
#print(type(sorted_customer))

orders = {}
for line in approvedorders:
    Customer_Name = line['Customer_Name']
    if Customer_Name in orders:
        orders[Customer_Name] += 1
    else:
        #no_of_orders = 1
        orders[Customer_Name] = 1

#print(orders.items())
#for key,value in orders.items():
    #print(key,value)


topcancelled = {}
for line in cancelledOrders:
    Product_Name = line['Product Name']
    if Product_Name in orders:
        topcancelled[Product_Name] += 1
    else:



        topcancelled[Product_Name] = 1

name = input("Enter the name:")

searchedlist = []
for line in sales_dict:
    if line['Customer_Name'] == name:
        searchedlist.append(line)

for line in searchedlist:
    print(line)
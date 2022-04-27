# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print(now.strftime("%H:%M:%S"))

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

print(type(current_time))
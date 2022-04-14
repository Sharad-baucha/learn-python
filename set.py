a = [1,2,3,4,5,6]
b = [1,3,5]
great  = a
small  = b
if len(b)> len(a):
    great = b
    small =  a
check = True
for i in range(len(small)):
    if small[i]not in  great:
        check= False
        break
if check== True:
    print("Sub-list")
else:
    print("Not sub-list")
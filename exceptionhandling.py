a = 5

try:
    print(a//0)
except Exception:
    print("Exception caught")
else:
    print("ahahhahah")
finally:
    print("inside finally")

print("Program executed")
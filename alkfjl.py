count = 0

my_string = "PRPRPJRPRPJPRPJRPjrpprprprprpprpr"
my_char = "r"

for i in my_string:
    if i == my_char or i == my_char.upper():
        count += 1

print(count)
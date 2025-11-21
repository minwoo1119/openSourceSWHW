import string
import random

length = 6
a = string.ascii_uppercase
result = "

for i in range(length):
    result += random.choice(a)

print(result)

import random
import string

len = 6
a = string.ascii_uppercase
result = ""

for i in range(len):
    result += random.choice(a)

print(result)

import random
import string

def random_generator():
    len = 6
    a = string.ascii_uppercase
    result = ""

    for i in range(len):
        result += random.choice(a)

    return result

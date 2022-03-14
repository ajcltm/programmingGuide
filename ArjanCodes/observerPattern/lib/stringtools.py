import string
import random

def get_random_string(num: int):
    string_pool = string.digits
    random_string = ""
    for i in range(num):
        random_string += random.choice(string_pool)
    return random_string
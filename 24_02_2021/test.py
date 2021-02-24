import random
import string

with open("random.txt", "w" ) as f:
    letters = string.ascii_lowercase
    letters1 = ''.join(random.choice(letters) for i in range(10)) + '\n'
    for i in range(4):
        f.write(letters1)
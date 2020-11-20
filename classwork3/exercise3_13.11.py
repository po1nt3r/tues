import math

def f(n):
    num1 = n
    i = 0
    while num1 >= 2:
        num1 = math.sqrt(num1)
        i += 1
    return i

num = int(input("Enter a number: "))

count = f(num)

print(num,'->',count)
import math

num = int(input("Enter a number: "))
num1 = num
count = 0
while num >= 2:
    num = math.sqrt(num)
    count += 1

print(num1,'->',count)
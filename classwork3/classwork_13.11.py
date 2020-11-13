import math

#задача 1
'''
a = input('Enter a string: ')
vowels = ['A','a','E','e','I','i','O','o','U','u']
a = list(a)

for i in vowels:
    for j in range(len(a)):
        if i == a[j]:
            for k in range(j, 3+j, 1):
                a.insert(k, i)

a = ''.join(a)

print(a)
'''
#задача 2
'''
num = int(input())
count = 0

while num != 0:
    num //= 10
    count += 1

print('Lenght ->', count)
'''
#задача 3
'''
num = int(input("Enter a number: "))
num1 = num
count = 0
while num >= 2:
    num = math.sqrt(num)
    count += 1

print(num1,'->',count)
'''
#задача 4
'''
num = int(input("Enter a number: "))
prime = True
add = 0
for i in range(2, num):
    prime = True
    for j in range(2,(i//2)+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)
        add += i

print(num,'->',add)
'''

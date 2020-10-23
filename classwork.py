'''
задача 1
a = input('Enter a number: ')

x =  1
while x < int(a):
    print(x)
    x+=1
'''
'''
задача 2
a = [1,2,3,6,4,5,8,96,5,56,56,65,6]

for x in range(len(a)):
    if a[x] % 2 == 0:
        print(str(a[x]) + 'is even')
    else:
        print(str(a[x]) + "is not even")
'''
a = input('Enter a number: ')
prime = True
x = 1
while x < int(a):
    if x > 1:
        for i in range(2, x//2+1):
            if (x % i) == 0:
                prime = False
                print(x, "is not a prime number")
                break

        if(prime == True):
            print(x, ' is prime')
    else:
        print('One is neither')
    
    x+=1
    
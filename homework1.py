'''
x = 0
y = 0
z = []
for i in range(2000, 5001):
    x = 0
    y = i
    z.clear()
    for j in range(4):
        if ((y % 10) % 2) == 0:
            x += 1
            z.append((y % 10))
        y //= 10
    z.reverse()
    if x == 4:
        print(i, end = ':')
        for j in range(len(z)):
            if j != 3:
                print(z[j], end=',')
            else:
                print(z[j])    
'''

'''
n = input('How many numbers do you want to enter: ')
z = []
for i in range(int(n)):
    z.append(input('Enter number:'))
min = int(z[0])
max = int(z[0])

for i in z:
    if int(i) > max:
        max = int(i)
    elif int(i) < min:
        min = int(i)

print(max - min)
'''

'''
str = input('Enter a string: ')
y = ''

str = list(str)
str.sort()
print(str)
for i in range(len(str)):
    print(i)
    if str[i] != y:
        print('\'', str[i], '\'', 'appears', str.count(str[i]), 'times in this string')
    y = str[i]
'''
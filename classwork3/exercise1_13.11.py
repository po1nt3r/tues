a = input('Enter a string: ')
vowels = ['A','a','E','e','I','i','O','o','U','u']
a = list(a)
j = 0

while j < len(a):
    for i in vowels:
        if a[j] == i:
            for k in range(j, j+3):
                a.insert(k, i)
                print('lenth of a: ' , len(a))
            j += 3
            print(j)
    j += 1
a = ''.join(a)
print(a)
num = int(input("Enter a number: "))
count = int(input("Enter how many numbers: "))

print(num, ',', count, end='->')

for i in range(1, count+1, 1):
    if(i != count):
        print(i*num, end=', ')
    else:
        print(i*num)
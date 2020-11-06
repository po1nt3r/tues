num = input("Enter a number: ")
num = list(num)
j = len(num)-1
count = 0
symmetrical = False

if len(num) > 1:
    for i in range(len(num)//2):
        if num[i] == num[j]:
            count += 1
        j-=1
    
    if count == len(num)//2:
        symmetrical = True

    if symmetrical:
        print(''.join(num), 'is symmetrical')
    else:
        print(''.join(num), 'is asymmetrical')
else:
    print('Single digit numbers are not symetrical neither asymmetrical')
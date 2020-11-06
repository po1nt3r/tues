'''
num = int(input("Enter a number: "))
n = 1
pr = n-1
nxtN = pr + n
print(0, 1, end=" ")
while nxtN < num:
    print(nxtN)
    pr = n
    n = nxtN
    nxtN = n + pr
'''

'''
string = input("Enter a string: ")    
num = int(input("Enter a number: "))

x = []
a = 0 
for i in range(0, len(string), len(string)//num):  
    if i != 0:
        x.append(string[a:i])
        a = i   

x.append(string[a::])

print(x)
'''
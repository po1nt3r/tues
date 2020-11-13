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
        add += i

print(num,'->',add)
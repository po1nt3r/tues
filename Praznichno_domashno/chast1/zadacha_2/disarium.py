def disarium_func(n):
    pos = len(n)
    sum = 0
    n1 = int(n)
    
    while n1 != 0:
        sum += (n1%10)**pos
        n1 //= 10
        pos -= 1
    
    if sum == int(n):
        return True
    else:
        return False 

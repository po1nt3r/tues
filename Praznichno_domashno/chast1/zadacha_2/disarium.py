def disarium_func(n):
    pos = len(n)
    sum1 = 0
    n1 = int(n)
    
    while n1 != 0:
        sum1+= (n1%10)**pos
        n1 //= 10
        pos -= 1
    
    if sum1 == int(n):
        return True
    else:
        return False 

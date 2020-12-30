def nextPrime(n):
    prime = True
    while True:
        prime = True
        for i in range(2, n//2 + 1):
            if n % i == 0:
                prime = False
                break
        if prime == False:
            n+=1
        else:
            return n
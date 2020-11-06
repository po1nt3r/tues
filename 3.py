array = ["my", 1, "turtle", "explain", 3.14]
n = len(array)
i = 0
while i < n:
    if type(array[i]) == int or type(array[i]) == float:
        del array[i]
        i -= 1
        n -= 1
    i += 1
    
print(array)
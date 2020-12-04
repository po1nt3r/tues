a = input("Enter a number for a: ")
b = input("Enter a number for b: ")
c = input("Enter a number for c: ")

a = list(a)
b = list(b)
c = list(c)


def is_equal(a, b, c):
    num = str(int(a[len(a) - 1]) * int(b[len(b) - 1]))
    num = list(num)

    if int(num[len(num)-1]) == int(c[len(c)-1]):
        return True
    else:
        return False


print(f"Zadacha 1: {is_equal(a, b, c)}")


limit = int(input("Ogranichenie: "))
distance = int(input("Razstoqnie koeto trqbva da bude izminato: "))


def speeding(limit, distance):
    time1 = distance/(limit)
    time2 = distance/(limit + 15)

    return (time1 - time2)*60


print("Excersise 2: %.2f minutes" % (speeding(limit, distance)))

print("Zadacha 1: ")

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


print(f"\n{is_equal(a, b, c)}\n")

print("Zadacha 2: ")

limit = int(input("Enter limit: "))
distance = int(input("Enter distance: "))


def speeding(limit, distance):
    time1 = distance/(limit)
    time2 = distance/(limit + 15)

    return (time1 - time2)*60


print("\n%.2f minutes\n" % (speeding(limit, distance)))

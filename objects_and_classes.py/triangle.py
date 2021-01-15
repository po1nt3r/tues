class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def lenght(self):
        print(f"The lenght of the triangle is {self.a + self.b + self.c}")

asd = Triangle(10,10,10)
asd.lenght()
class Number:
    def __init__(self, num):
        self.number = num

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        self.number += other
        return Number(self.number)


# class
n = Number(10)
print(n)
n + 10
print(n)
n += 10
print(n)
print(type(n))

# primitive type
x = 10
print(x)
x += 10
print(x)
print(type(x))


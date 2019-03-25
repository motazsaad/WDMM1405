class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def __str__(self):
        return 'length: {}\twidth:{}'.format(self.length,self.width)

    def get_aria(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


rec1 = Rectangle(length=3, width=4)
print(rec1)

l1 = list()
l2 = list([1,3,4])
l3 = [1,5,8]
print(l1, l2, l3)
rec2 = Rectangle()
print(rec2)
rec3 = Rectangle(length=7, width=9)
print(rec3)

print('aria for', rec1, rec1.get_aria())
print('perimeter for', rec3, rec3.get_perimeter())
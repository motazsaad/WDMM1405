class Circle:
    def __init__(self, center=(0, 0), r=0):
        self.center = center
        self.r = r

    def __str__(self):
        return 'center:{}\tr:{}'.format(
            self.center, self.r
        )


c1 = Circle((3, 4), 3)
c2 = Circle(center=(2, 5), r=8)
print(c1, c2)

l1 = list()  # empty list
l2 = list([1, 4, 8])
l3 = [1, 5, 9]
print(l1, l2, l3)

c3 = Circle()
print(c3)
c4 = Circle(center=(1, 1))
print(c4)

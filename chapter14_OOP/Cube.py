class Cube:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return 'x = {}'.format(self.x)

    def area(self):
        return 6 * self.x * self.x

    def volume(self):
        return self.x * self.x * self.x


cube1 = Cube(3)
print(cube1)
print('surface area', cube1.area())
print('volume', cube1.volume())

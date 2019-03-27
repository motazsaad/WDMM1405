class Square:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return 'x = {}'.format(self.x)

    def area(self):
        return self.x * self.x

    def perimeter(self):
        return 4 * self.x


if __name__ == '__main__':
    s1 = Square(5)
    print(s1)
    print('area: ', s1.area())
    print('perimeter: ', s1.perimeter())

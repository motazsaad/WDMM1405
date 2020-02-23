from chapter14_OOP.Square import Square


# from dir.filename import class name
# self : pointer to the same class
# super() # pointer to the super class

class Cube(Square):  # child Cube, Parent: Square

    def area(self): # override
        return super().area() * 6

    def volume(self):
        return self.x ** 3


cube1 = Cube(3)
print(cube1)
print('area', cube1.area())
print('volume', cube1.volume())

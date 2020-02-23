class Rectangle:
    l = 0
    w = 0
    line_color = 'black'

    def __init__(self, length, width, color):
        self.l = length
        self.w = width
        self.line_color = color

    def get_aria(self):
        return self.l * self.w

    def get_perimeter(self):
        return 2 * (self.l + self.w)

    def __str__(self):
        return 'lenght = {}\nwidth = {}\ncolor: {}'.format(self.l, self.w, self.line_color)


rec1 = Rectangle(3,2,'blue')
rec2 = Rectangle(9,4,'red')

print(rec1)
print('aria', rec1.get_aria())

print(rec2)
print('perimeter', rec2.get_perimeter())
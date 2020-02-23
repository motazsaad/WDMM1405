class Person:
    name = None
    age = 0
    gender = None

    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g

    def walk(self):
        print('I am walking')

    def eat(self):
        print('I am eating :)')

    def __str__(self): # string representation of the object
        return 'name: {}\tage: {}\tgender: {}'.format(self.name, self.age, self.gender)


p1 = Person('Ahmed', 20, 'm')
p2 = Person('Attia', 25, 'm')
p1.walk()
p2.eat()

print(p1)
print(p2)

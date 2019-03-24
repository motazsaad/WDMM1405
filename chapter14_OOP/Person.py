class Person:
    name = None
    age = 0
    gender = None

    def __init__(self, name=None, age=0, gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print('I am walking')

    def eat(self):
        print('I am eating :) ')


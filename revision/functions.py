# function advantages
# 1. reuse code
# 2. simplify code

# verb phrase for functions
# def compute_sum(): # this is a good function name
# def car_speed(): # this is a bad function name
# def get_car_speed(): # this is a good function name
# def increase_car_speed(): # this is a good function name

# noun phrase for variables
car_speed = 10
# noun
car = 'BMW'


def add(x, y):
    return x + y


print(add(3, 4))  # call and print result
print(add(2, 7))  # call and print result
result = add(10, 3)  # call store results in a variable
result += 3  # flexibility
print(result)


# best practice (input and output are outside the function)
def say_hello(name):
    msg = 'hello ' + name
    msg += '\nwelcome to python II'
    return msg


print(say_hello('Ahmed'))
name1 = input('enter a name: ')
result = say_hello(name1)
result += '\npython is cool'
print(result)

# function advantages
# 1. reuse code
# 2. simplify code


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
aname = input('enter a name: ')
result = say_hello(aname)
result += '\npython \\nis cool'
print(result)

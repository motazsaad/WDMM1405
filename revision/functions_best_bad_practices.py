# bad practice: I/O inside the function
def say_hello():
    name = input('enter a name: ')
    print('hello ' + name)


# say_hello()


# best practice: No I/O in the function
def say_hello2(name):
    msg = 'hello ' + name
    msg += '\nPleased to meet you'
    return msg


print(say_hello2('Ahmed'))
name1 = input('enter a name: ')
result = say_hello2(name1)
result += '\nWelcome to python II'
print(result)

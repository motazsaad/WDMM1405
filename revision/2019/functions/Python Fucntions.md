
# Python Functions 
## function advantages
1. Reuse code
2. Simplify code

## Funtion names 
* verb phrase for functions
* def compute_sum(): # this is a good function name
* def car_speed(): # this is a bad function name
* def get_car_speed(): # this is a good function name
* def increase_car_speed(): # this is a good function name

# Bad practice: I/O inside the function
This is a restriction. You force me to provide the input in the CLI, and the function provides the result on the CLI


```python
def say_hello():
    name = input('enter a name: ')
    print('hello ' + name)
```


```python
# call the function
say_hello()
```

    enter a name: Ahmed
    hello Ahmed
    

# Best practice (input and output are outside the function)

This is not only for python, this paractice is good for all programming language 


```python
# best practice (input and output are outside the function)
def add(x, y):
    return x + y
```


```python
print(add(3, 4))  # call and print result
```

    7
    


```python
print(add(2, 7))  # call and print result
```

    9
    


```python
result = add(10, 3)  # call store results in a variable
result += 3  # flexibility
print(result)
```

    16
    


```python
# best practice (input and output are outside the function)
def say_hello(name):
    msg = 'hello ' + name
    msg += '\nwelcome to python II'
    return msg
```


```python
print(say_hello('Ahmed'))
```

    hello Ahmed
    welcome to python II
    


```python
name1 = input('enter a name: ')
result = say_hello(name1)
result += '\npython is cool'
print(result)
```

    enter a name: Ali
    hello Ali
    welcome to python II
    python is cool
    

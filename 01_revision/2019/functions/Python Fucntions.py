#!/usr/bin/env python
# coding: utf-8

# # Python Functions 
# ## function advantages
# 1. Reuse code
# 2. Simplify code
# 
# ## Funtion names 
# * verb phrase for functions
# * def compute_sum(): # this is a good function name
# * def car_speed(): # this is a bad function name
# * def get_car_speed(): # this is a good function name
# * def increase_car_speed(): # this is a good function name

# # Bad practice: I/O inside the function
# This is a restriction. You force me to provide the input in the CLI, and the function provides the result on the CLI

# In[1]:


def say_hello():
    name = input('enter a name: ')
    print('hello ' + name)


# In[2]:


# call the function
say_hello()


# # Best practice (input and output are outside the function)
# 
# This is not only for python, this paractice is good for all programming language 

# In[3]:


# best practice (input and output are outside the function)
def add(x, y):
    return x + y


# In[4]:


print(add(3, 4))  # call and print result


# In[5]:


print(add(2, 7))  # call and print result


# In[6]:


result = add(10, 3)  # call store results in a variable
result += 3  # flexibility
print(result)


# In[7]:


# best practice (input and output are outside the function)
def say_hello(name):
    msg = 'hello ' + name
    msg += '\nwelcome to python II'
    return msg


# In[8]:


print(say_hello('Ahmed'))


# In[9]:


name1 = input('enter a name: ')
result = say_hello(name1)
result += '\npython is cool'
print(result)


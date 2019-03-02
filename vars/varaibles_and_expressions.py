#!/usr/bin/env python
# coding: utf-8

# # Python Variables and Experissions

# # Variables are names of places in memory 
# Since it is variable, then the values changes 

# # Reserve a place in memory named x and store the value 10 in it. 

# In[1]:


x = 10


# # Variables should be defined before using them 

# In[2]:


print(y) # name error because y is not defined 


# In[3]:


y = 20 
print(y) # now it is OK :) 


# # Variable names should meaningful 
# names should be nouns or noun phrases 

# In[4]:


car_speed = 10 # good name 
car = 'BMW' # good name 
name = 'Ahmed' # good name 
a = 10 # bad name


# # Naming variables in Python 
# 1. shoud start with _ or letter 
# 2. variables are case sentsetive
# 3. No special charachters 

# In[5]:


car1 = 'BMW' # good name 


# In[6]:


1car = 'BMW' # bad name (syntax error )


# In[7]:


car$speed = 100 # bad name (syntax error)


# # Statements

# In[8]:


x = 10  # assignment


# In[9]:


y = x + 3  # expression and assignment


# # Experssions 

# In[10]:


print(2 ** 3)  # power: 2*2*2


# In[11]:


print(divmod(23, 5))  # (4, 3)


# In[12]:


print(23 // 5)  # 4


# In[13]:


print(23 % 5)  # 3


# # Operator Precedence Rules
# 
# * Parentheses are always respected
# * Exponentiation (raise to a power)
# * Multiplication, Division, and Remainder
# * Addition and Subtraction
# * Left to right
# 

# In[14]:


x = 0.6
3.9 *  x  * ( 1  -  x )


# # Python Types int, float, str

# In[15]:


x = 10
print(type(x))  # <class 'int'>


# In[16]:


x = 10.1
print(type(x))  # <class 'float'>


# In[17]:


x = 'abc'
print(type(x))  # <class 'str'>


# # int / int = always result is float number 

# In[18]:


print(10 / 3)  # float result
print(10 / 2)  # float result


# # String concat 

# In[19]:


print('abc' + '123')  # concat


# In[20]:


print('abc' - 'qwerty') # error


# # Type conversions

# In[21]:


# int to str 
print(str(123))


# In[22]:


# flaot to str 
print(str(12.3))


# In[23]:


# str to int 
print(int('133'))


# In[24]:


print(int('133abc')) # error 


# In[25]:


print(int('13.3')) # error 


# In[26]:


# string to flaot 
print(float('13.3'))


# In[27]:


print(float('13.3.1')) # error 


#!/usr/bin/env python
# coding: utf-8

# # Re-implement some Python built-in functions

# In[1]:


def my_max(l1):
    max_number = l1[0]
    for number in l1:
        if number > max_number:
            max_number = number
    return max_number


# In[2]:


def my_mix(l1):
    mix_number = l1[0]
    for number in l1:
        if number < mix_number:
            mix_number = number
    return mix_number


# In[3]:


def my_sum(l1):
    total = 0
    for number in l1:
        total += number
    return total


# In[4]:


def my_len(l1):
    count = 0
    for i in l1:
        count += 1
    return count


# In[5]:


def my_divmod(x, y):
    result = x // y
    reminder = x % y
    return result, reminder


# In[6]:


def my_power(x, y):
    return x ** y


# In[7]:


def my_abs(x):
    if x >= 0:
        return x
    else:
        return x * -1 


# # calls 

# In[8]:


print(my_max([1, 2, 5]))


# In[9]:


print(my_mix([1, 2, 5]))


# In[10]:


print(my_sum([1, 2, 5]))


# In[11]:


print(my_len([1, 2, 5]))


# In[12]:


print(my_divmod(23, 5))


# In[13]:


print(my_power(23, 5))


# In[14]:


print(my_abs(-12))


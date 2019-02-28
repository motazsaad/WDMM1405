#!/usr/bin/env python
# coding: utf-8

# # Python Decisions

# # One way decision 

# In[1]:


x = 25
if x > 10:
    print('big')
    print('it is big')
print('done')


# In[2]:


x = 2
if x > 10:
    print('big')
    print('it is big')
print('done')


# # Two ways decision 

# In[3]:


x = 25
if x > 10:
    print('big')
    print('it is big')
else:  # x <=10
    print('small')
    print('it is small')
print('done')


# In[4]:


x = 7
if x > 10:
    print('big')
    print('it is big')
else:  # x <=10
    print('small')
    print('it is small')
print('done')


# # Multi-ways decisions 

# In[5]:


x = 15
if x > 10:
    print('big')
    print('it is big number')
elif x < 5:  # x <= 10
    print('small')
    print('it is small')
else:
    print('between 5 and 10')
print('done')


# In[6]:


x = 7
if x > 10:
    print('big')
    print('it is big number')
elif x < 5:  # x <= 10
    print('small')
    print('it is small')
else:
    print('between 5 and 10')
print('done')


# In[7]:


x = 3
if x > 10:
    print('big')
    print('it is big number')
elif x < 5:  # x <= 10
    print('small')
    print('it is small')
else:
    print('between 5 and 10')
print('done')


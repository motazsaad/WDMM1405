#!/usr/bin/env python
# coding: utf-8

# # Tuples

# In[1]:


friend_list = ['Ahmed', 'Ali', 'Samer']  # list

# In[2]:


friend_list[1]

# In[3]:


friend_tuple = ('Ahmed', 'Ali', 'Samer')  # tuple

# In[4]:


friend_tuple[1]

# In[5]:


for name in friend_tuple:  # loop using iteration variable
    print(name)

# In[7]:


for i in range(len(friend_tuple)):  # loop using index
    print(friend_tuple[i])

# # A tuple is a list but ...
# 1. Immutable
# 2. Simpler and more efficient in terms of memory use and performance than lists (faster) 

# In[8]:


friend_tuple[2] = 'Mohammed'  # error tuples are immputable

# In[9]:


friend_list[2] = 'Mohammed'  # mutable
print(friend_tuple)

# # Tuple assignment

# In[10]:


(x, y) = (4, 'fred')

# In[11]:


x

# In[12]:


y


# In[13]:


def my_divmod(x, y):
    reminder = x % y
    result = x // y
    return reminder, result


# In[14]:


my_divmod(23, 5)

# In[15]:


(a, b) = my_divmod(23, 5)

# In[16]:


a

# In[17]:


b

# In[18]:


bag = {'books': 1, 'candy': 3, 'pen': 1}

# In[19]:


bag.items()

# In[20]:


for k, v in bag.items():
    print('{}\t{}'.format(k, v))

# In[21]:


(0, 1, 2) < (5, 1, 2)

# In[22]:


(0, 1, 3) < (5, 1, 2)

# In[23]:


(0, 1, 2000000) < (0, 3, 4)

# In[24]:


(1, 1, 2000000) < (0, 3, 4)

# In[25]:


('Jones', 'Sally') < ('Jones', 'Sam')

# In[26]:


d = {'a': 10, 'c': 22, 'b': 1}
d.items()

# In[27]:


sorted(d.items())

# In[28]:


sorted(d.items(), reverse=True)

# # Sort dictionary using the values

# In[29]:


tmp = list()
for k, v in d.items():
    tmp.append((v, k))
print(tmp)

# In[30]:


sorted(tmp)

# In[31]:


sorted(tmp, reverse=True)

# # Sort Dictionary by values in one line

# In[33]:


sorted([(v, k) for k, v in d.items()])

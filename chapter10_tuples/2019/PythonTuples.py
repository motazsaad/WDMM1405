#!/usr/bin/env python
# coding: utf-8

# # Python Tuples

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

# In[6]:


for i in range(len(friend_tuple)):  # loop using index
    print(friend_tuple[i])

# # A tuple is a list but ...
# 1. Immutable
# 2. Simpler and more efficient in terms of memory use and performance than lists (faster) 

# In[7]:


friend_tuple[2] = 'Mohammed'  # error tuples are immputable


# In[8]:


friend_list[2] = 'Mohammed'  # mutable
print(friend_list)

# # Tuple assignment

# In[9]:


(x, y) = (4, 'fred')


# In[10]:


x


# In[11]:


y


# In[12]:


def my_divmod(x, y):
    reminder = x % y
    result = x // y 
    return reminder, result


# In[13]:


my_divmod(23, 5)


# In[14]:


(a, b) = my_divmod(23, 5)


# In[15]:


a


# In[16]:


b


# In[17]:


bag = {'books': 1, 'candy': 3, 'pen': 1}


# In[18]:


bag.items()

# In[19]:


for k, v in bag.items():
    print('{}\t{}'.format(k, v))

# # Tuple Comparison

# In[20]:


(0, 1, 2) < (5, 1, 2)


# In[21]:


(0, 1, 3) < (5, 1, 2)

# In[22]:


(0, 1, 2000000) < (0, 3, 4)

# In[23]:


(1, 1, 2000000) < (0, 3, 4)


# In[24]:


('Jones', 'Sally') < ('Jones', 'Sam')


# In[25]:


d = {'a': 10, 'c': 22, 'b': 1}
d.items()

# # Sort dictionary by keys

# In[26]:


sorted(d.items())


# In[27]:


sorted(d.items(), reverse=True)


# In[28]:


# can't compare different types 
3 > 'a'

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

# In[32]:


sorted([(v, k) for k, v in d.items()])

# In[33]:


sorted([(v, k) for k, v in d.items()], reverse=True)

# In[34]:


# top n elements 
sorted([(v, k) for k, v in d.items()], reverse=True)[:2]

# Write a program take an input from the user and to:
# 1. print the word counts sorted alpabetically 
# 2. print the top 5 most frequent words 

# In[35]:


text = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
words = text.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

# In[36]:


# 1. print the word counts sorted alpabetically
print(sorted(counts.items()))

# In[37]:


# 2. print the top 5 most frequent words 
print(sorted([(v, k) for k, v in counts.items()], reverse=True)[:5])

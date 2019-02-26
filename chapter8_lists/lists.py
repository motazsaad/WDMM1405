#!/usr/bin/env python
# coding: utf-8

# # primitive data: one value in variable 

# In[3]:


x = 10
print(x)
x = 20
print(x)

# # store more than one value in one variable (collection)

# In[4]:


x = [10, 20]
print(x)

# # differet types in one collection

# In[11]:


# differet types in one collection 
x = [10, 'Ahmed']
print(x)

# # list constant

# In[12]:


# list constant 
print(3)
print([1, 24, 76])

# In[13]:


# different types: str, int, float
print(['red', 24, 98.6])

# # list in a list / collection in a collection

# In[15]:


x = [1, [5, 6], 7]
print(x)
print(x[0])
print(x[1])
print(x[1][0])

# # Empty list

# In[16]:


# empty list 
x = []
print(x)

# # iteration variable

# In[18]:


# iteration variable 
for num in [5, 4, 3, 2, 1]:
    print(num)
print('Blastoff!')

# In[19]:


# iteration variable 
friends = ['Joseph', 'Glenn', 'Sally']
for name in friends:
    print('Happy New Year:', name)
print('Done!')

# In[22]:


# access elements by index 
print(friends[1])

# # mutable list: we can change the value of list elements

# In[23]:


# mutable list 
friends[1] = 'Ahmed'
print(friends)

# # imutable list (list of characters)

# In[31]:


# imutable list 
fruite = 'banana'
print(fruite)
print(fruite[1])
# fruite[1] = 'e'
# convert to mutable 
f = list(fruite)
print(f)  # mutable
f[1] = 'e'
print(f)
fruite = str(''.join(f))
print(fruite)

# # join a list of numbers

# In[2]:


# join list 
l1 = [1, 3, 10, 19]
print(l1)
l2 = [str(x) for x in l1]
print(';'.join(l2))

# # loop on a list: way 1: iteration variable

# In[3]:


# loop on list 
friends = ['Joseph', 'Glenn', 'Sally']
# way 1: iteration variable 
for friend in friends:
    print('Happy New Year:', friend)

# # loop on a list: way 2: using index

# In[5]:


# loop on list 
friends = ['Joseph', 'Glenn', 'Sally']
# way 2: index 
for i in range(len(friends)):
    print('Happy New Year:', friends[i])

# # list concatonation

# In[39]:


a = [1, 2, 3]
b = [4, 5, 6]
# concat 
c = a + b
print(c)
# d = a - b # error 


# # sum 2 lists 

# In[40]:


# sum 2 lists 
a = [1, 2, 3]
b = [4, 5, 6]
c = [a[i] + b[i] for i in range(len(a))]
print(c)

# # slicing a list

# In[47]:


# slicing a list 
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t[2:4])  # index 2, 3
print(t[2:])  # index 2 to the end
print(t[:4])  # index 0 to 3

# # list mehtods

# In[6]:


# list mehtods 
t = [9, 41, 12, 3, 74, 15]
print(dir(t))

# # append functions

# In[49]:


print(t)
t.append(10)  # add 3 to the end of the list
print(t)

# # sum 2 lists using empty list with append

# In[52]:


# sum 2 lists using empty list with append 
a = [1, 2, 3]
b = [4, 5, 6]
c = []
print('before sum: c = ', c)
list_size = len(a)
for i in range(list_size):
    r = a[i] + b[i]
    c.append(r)
    print(i, c)

# # count function

# In[65]:


# count 
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t.count(3))
print(t.count(74))
t.append(3)
print(t)
print(t.count(3))

# # extend function

# In[7]:


print(t)
t.extend([1, 2, 5])  # similar to t + [1, 2, 5]
print(t)

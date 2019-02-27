#!/usr/bin/env python
# coding: utf-8

# # Programming
# * Algorithm  A set of rules or steps used to solve a problem
# 
# * Data Structure  -  A particular way of organizing data in a computer
# 

# # primitive data: one value in variable
# 
# primitive data type: int, float, str 
# بيانات أولية وليست تجميعية ، فقط استطيع تخزين قيمة واحدة في المتغير 

# In[1]:


x = 10 
print(x)
x = 20 
print(x)


# # store more than one value in one variable (collection)
# List is a collect. We can store many values in one variable 

# In[2]:


x = [10, 20]
print(x)
print(type(x))


# # different  types in one collection 

# In[3]:


# differet types in one collection 
x = [10, 'Ahmed']
print(x)


# In[4]:


# different types: str, int, float
print(['red', 24, 98.6])


# # list constant 

# In[5]:


# list constant 
print(3)
print([1, 24, 76])


# # list in a list / collection in a collection 

# In[6]:


x = [1, [5, 6], 7]
print(x)
print(x[0])
print(x[1])
print(x[1][0])


# # Empty list 

# In[7]:


# empty lists 
x = []
y = list()
print('x = ', x)
print('y = ', y)


# In[8]:


# Empty String 
empty_str = ''
print(empty_str)


# # iteration variable 

# In[9]:


# iteration variable 
for num in [5, 4, 3, 2, 1] :
    print(num)
print('Blastoff!')


# In[10]:


# iteration variable 
friends = ['Joseph', 'Glenn', 'Sally']
for name in friends:
    print('Happy New Year:',  name)
print('Done!')


# In[11]:


# access elements by index 
print(friends[1])


# # mutable list: we can change the value of list elements 

# In[12]:


# mutable list 
friends[1] = 'Ahmed'
print(friends)


# # immutable list (list of characters)

# In[13]:


# immutable list 
fruit = 'banana'
print(fruit)


# In[14]:


print(fruit[1])
# fruite[1] = 'e' # error 


# In[15]:


# convert to mutable 
f = list(fruit)
print(f) # mutable 
f[1] = 'e'
print(f)


# In[16]:


fruit = str(''.join(f))
print(fruit)


# # join a list of numbers 

# In[17]:


# join list 
l1 = [1, 3, 10, 19]
print(l1)
l2 = [str(x) for x in l1]
print(';'.join(l2))


# # loop on a list: way 1: iteration variable 

# In[18]:


# loop on list 
friends = ['Joseph', 'Glenn', 'Sally']
# way 1: iteration variable 
for friend in friends :
    print('Happy New Year:',  friend)


# # loop on a list: way 2: using index 

# In[19]:


# loop on list 
friends = ['Joseph', 'Glenn', 'Sally']
# way 2: index 
for i in range(len(friends)) :
    print('Happy New Year:',  friends[i])


# # list concatonation 

# In[20]:


a = [1, 2, 3]
b = [4, 5, 6]
# concat 
c = a + b 
print(c)
# d = a - b # error 


# # sum 2 lists 

# In[21]:


# sum 2 lists 
a = [1, 2, 3]
b = [4, 5, 6]
c = [a[i] + b[i] for i in range(len(a))] # using index 
print(c)


# In[22]:


# sum 2 lists 
a = [1, 2, 3]
b = [4, 5, 6]
c = [m + n for m, n in zip(a, b)] # using iteration variables  
print(c)


# # Understanding zip function 

# In[23]:


a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))


# # slicing a list 

# In[24]:


# slicing a list 
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t[2:4]) # index 2, 3 
print(t[2:]) # index 2 to the end 
print(t[:4]) # index 0 to 3 


# # list methods 

# In[25]:


# list mehtods 
t = [9, 41, 12, 3, 74, 15]
print(dir(t))


# # append functions 

# In[26]:


print(t)
t.append(10) # add 3 to the end of the list 
print(t)


# # sum 2 lists using empty list with append 

# In[27]:


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

# In[28]:


# count 
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t.count(3))
print(t.count(74))
t.append(3)
print(t)
print(t.count(3))


# # extend function

# In[29]:


print(t)
t.extend([1, 2, 5]) # similar to t + [1, 2, 5]
print(t)


# # index function

# In[30]:


print(t)
t.index(15)
# t.index(5) # does not exist --> value error 


# # insert function 

# In[31]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.insert(3, 5) # insert 5 at index 3 
print(t)


# # pop function 

# In[32]:


t = [9, 41, 12, 3, 74, 15]
print(t)
print(t.pop())
print(t)


# # remove function

# In[33]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.remove(12)
print(t)
t.append(3)
print(t)
t.remove(3) # remove the first match 
print(t)


# # reverse function 

# In[34]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.reverse()
print(t)


# # sort function 

# In[35]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.sort()
print(t)
t.sort(reverse=True)
print(t)


# # Is Something in a List?

# In[36]:


t = [9, 41, 12, 3, 74, 15]
print(t)
12 in t


# In[37]:


5 in t


# # Built-in Functions and Lists

# In[38]:


nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


# # split a string with a lot of spaces 

# In[39]:


line = 'A lot               of spaces'
line.split()


# # split a string using a delimter 

# In[40]:


line = 'first;second;third'
line.split(';')


#!/usr/bin/env python
# coding: utf-8

# # Programming
# * Algorithm  A set of rules or steps used to solve a problem
# 
# * Data Structure  -  A particular way of organizing data in a computer
# 

# # Primitive data: one value in variable
# 
# primitive data type: int, float, str 
# بيانات أولية وليست تجميعية ، فقط استطيع تخزين قيمة واحدة في المتغير 

# In[1]:


x = 10 
print(x)
x = 20 
print(x)


# # Store more than one value in one variable (collection)
# List is a collect. We can store many values in one variable 

# In[2]:


x = [10, 20]
print(x)
print(type(x))


# # Different  types in one collection 

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


# In[7]:


print(x[0])


# In[8]:


print(x[1])


# In[9]:


print(x[1][0])


# # Empty list 

# In[10]:


# empty lists 
x = []
y = list()
print('x = ', x)
print('y = ', y)


# In[11]:


# Empty String 
empty_str = ''
print(empty_str)


# # iteration variable 

# In[12]:


# iteration variable 
for num in [5, 4, 3, 2, 1] :
    print(num)
print('Blastoff!')


# In[13]:


# iteration variable 
friends = ['Joseph', 'Glenn', 'Sally']
for name in friends:
    print('Happy New Year:',  name)
print('Done!')


# # Looking inside the list
# ![image.png](attachment:image.png)

# In[14]:


# loop using index
friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    print('Happy New Year:',  friends[i])
print('Done!')


# In[15]:


# access elements by index 
print(friends[1])


# # mutable list: we can change the value of list elements 

# In[16]:


# mutable list 
friends[1] = 'Ahmed'
print(friends)


# # immutable list (list of characters)

# In[17]:


# immutable list 
fruit = 'banana'
print(fruit)


# In[18]:


print(fruit[1])
fruit[1] = 'e' # error 


# In[ ]:


# convert to mutable 
f = list(fruit)
print(f) # mutable 
f[1] = 'e'
print(f)


# In[ ]:


fruit = ''.join(f)
print(fruit)


# # join a list of numbers 

# In[ ]:


# join list 
l1 = [1, 3, 10, 19]
print(l1)
l2 = [str(n) for n in l1]
print('\t'.join(l2))


# # loop on a list: way 1: iteration variable 

# In[ ]:


# loop on list 
friends = ['Joseph', 'Glenn', 'Sally']
# way 1: iteration variable 
for friend in friends :
    print('Happy New Year:',  friend)


# # loop on a list: way 2: using index 

# In[ ]:


# loop on list 
friends = ['Joseph', 'Glenn', 'Sally']
# way 2: index 
for i in range(len(friends)) :
    print('Happy New Year:',  friends[i])


# # list concatonation 

# In[ ]:


a = [1, 2, 3]
b = [4, 5, 6]
# concat 
c = a + b 
print(c)


# In[ ]:


d = a - b # error 


# # sum 2 lists 

# In[ ]:


# sum 2 lists 
a = [1, 2, 3]
b = [4, 5, 6]
c = [a[i] + b[i] for i in range(len(a))]  # using index 
print(c)


# In[ ]:


# sum 2 lists 
a = [1, 2, 3]
b = [4, 5, 6]
c = [m + n for m, n in zip(a, b)] # using iteration variables  
print(c)


# # Understanding zip function 

# In[ ]:


a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))


# # slicing a list 

# In[ ]:


# slicing a list 
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t[2:4]) # index 2, 3 


# In[ ]:


print(t[2:]) # index 2 to the end 


# In[ ]:


print(t[:4]) # index 0 to 3 


# # list methods 

# In[ ]:


# list mehtods 
t = [9, 41, 12, 3, 74, 15]
print(dir(t))


# # Append functions 

# In[ ]:


print(t)
t.append(10) # add 3 to the end of the list 
print(t)


# # Sum 2 lists using empty list with append 

# In[ ]:


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
    
# in one line 
# c = [a[i] + b[i] for i in range(len(a))] 
# c = [m + n for m, n in zip(a, b)]


# # Count function 

# In[ ]:


# count 
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t.count(3))


# In[ ]:


print(t.count(13))


# In[ ]:


print(t.count(74))


# In[19]:


t.append(3)
print(t)
print(t.count(3))


# # Extend function

# In[ ]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.extend([1, 2, 5]) # similar to t + [1, 2, 5] # like concat 
print(t)


# # extend vs append

# In[ ]:


# extend vs append 
t = [9, 41, 12, 3, 74, 15]
t.append([1, 2, 5])
print(t)


# # Index function

# In[ ]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.index(15)


# In[ ]:


t.index(5) # does not exist --> value error 


# # Insert function 

# In[ ]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.insert(3, 5) # insert 5 at index 3 
print(t)


# # Pop function 

# In[ ]:


t = [9, 41, 12, 3, 74, 15]
print(t)
print(t.pop())
print(t)


# # Remove function

# In[20]:


t = [9, 41, 12, 3, 74, 15, 3]
print(t)
t.remove(12)
print(t)


# In[21]:


t = [9, 41, 12, 3, 74, 15, 3]
print(t)
t.remove(3) # remove the first match 
print(t)


# In[22]:


t.remove(70) # error 


# # Reverse function 

# In[32]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.reverse()
print(t)


# # Sort function 

# In[33]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.sort()
print(t)


# In[34]:


t = [9, 41, 12, 3, 74, 15]
print(t)
t.sort(reverse=True)
print(t)


# # Is Something in a List?

# In[35]:


t = [9, 41, 12, 3, 74, 15]
print(t)
12 in t


# In[36]:


5 in t


# # Built-in Functions and Lists

# In[37]:


nums = [3, 41, 12, 9, 74, 15]
print(len(nums))


# In[38]:


print(max(nums))


# In[39]:


print(min(nums))


# In[40]:


print(sum(nums))


# In[41]:


print(sum(nums)/len(nums))


# # split a string with a lot of spaces 

# In[42]:


line = 'A lot               of spaces' # white space 
line.split()


# # Split a string using a delimter 

# In[43]:


line = 'first;second;third'
line.split(';')


# In[44]:


line = '10\t13\t25'
numbers = line.split('\t')
print(numbers)


# In[45]:


int_numbers = [int(n) for n in numbers]
print(int_numbers)


# In[46]:


print(sum(int_numbers))


# # Handle mail box

# In[47]:


line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)


# In[48]:


email = words[1]
print(email)


# In[49]:


pieces = email.split('@')
print(pieces)


# In[50]:


year = words[-1]
print(year)


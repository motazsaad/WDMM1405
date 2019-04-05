#!/usr/bin/env python
# coding: utf-8

# In[1]:


# the list
l1 = [1, 3, 4, 7, 3, 9, 3]

# # change all 3s to 13

# In[2]:


print('before', l1)
for i in range(len(l1)):
    if l1[i] == 3:
        l1[i] = 13
print('after', l1)

# # add 2 for every elements that is larger than 5

# In[3]:


print('before', l1)
for i in range(len(l1)):
    if l1[i] > 5:
        l1[i] += 2
print('after', l1)

# # find the position of the value 9 in the list

# In[9]:


for i in range(len(l1)):
    if l1[i] == 9:
        print(i)

# # find the average

# In[5]:


total = 0
count = 0
for n in l1:  # iteration variable, no need for the index
    total += n
    count += 1
print('average', total / count)

# # search for a number

# In[6]:


print(l1)
key = int(input('enter a number: '))
for i in range(len(l1)):
    if l1[i] == key:
        print(i)
        break

# # find the max value

# In[8]:


print(l1)
max = l1[0]
for i in range(len(l1)):
    if l1[i] > max:
        max = l1[i]
print('max:', max)

# # Find the sum

# In[10]:


total = 0
for n in l1:  # no need for index
    total += n
print('total=', total)

# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# # Dictionaries 

# In[1]:


l1 = [120171122, 'Ahmed', 'MM Dept', '1']
# index 0 : student id 
# index 1 : student name 
# index 2 : department 
# ....


# In[2]:


dic = {}
print(dic)

# In[3]:


# add using label (key)
# dic[0] use index in list but not in dictionary 
dic['id'] = 120171122  # key = id, value = 120171122
dic['name'] = 'Ahmed'
dic['dept'] = 'MM'
print(dic)

# # Dictionary
# key : value 

# # what is in your bag 

# In[4]:


bag = {'tissue': 5, 'money': 15, 'candy': 3, 'books': 0, 'laptop': 1}
print(bag)

# In[5]:


bag_list = [5, 15, 3, 0, 1]

# In[6]:


bag['money'] = 30
print(bag)

# In[7]:


bag['phone'] = 1
print(bag)

# In[8]:


bag['candy'] += 2
print(bag)

# In[9]:


print(bag['tissue'])

# In[10]:


print(bag['pen'])

# In[11]:


# if key in dictonary: 
if 'pen' in bag:
    print(bag['pen'])

# In[12]:


'pen' in bag

# In[13]:


# key in dictionary 
'candy' in bag

# In[14]:


# the value of the key 
bag['candy']

# In[15]:


bag.get('pen')

# In[16]:


print(bag.get('pen'))

# In[17]:


bag.get('pen', 0)

# In[18]:


bag.get('pen', 'not found')

# In[19]:


bag.get('candy', 0)

# In[20]:


bag.get('candy', 'not found')

# In[22]:


names = ['ahmed', 'mohammed', 'ali', 'hassan', 'khalid', 'ahmed', 'mohammed']
print(names)

# In[23]:


name_dict = dict()  # same as name_count = {}
for name in names:
    if name in name_dict:
        name_dict[name] += 1
    else:
        name_dict[name] = 1
print(name_dict)

# In[24]:


name_dict['ahmed']

# In[26]:


name_dict['khalid']

# In[28]:


# name_dict['mahmood']
name_dict.get('mahmood', 0)

# In[29]:


name_dict.get('mahmood', 'not found')

# In[30]:


# find name count using get 
name_dict = dict()  # same as name_count = {}
for name in names:
    name_dict[name] = name_dict.get(name, 0) + 1
print(name_dict)

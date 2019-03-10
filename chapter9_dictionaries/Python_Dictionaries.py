#!/usr/bin/env python
# coding: utf-8

# # Dictionaries 

# In[36]:


l1 = [120171122, 'Ahmed', 'MM Dept', 1]
# index 0 : student id 
# index 1 : student name 
# index 2 : department 
# ....
print('department:', l1[2])
print('name:', l1[1])


# In[2]:


dic = {}
print(dic)

# In[38]:


# add using label (key)
# dic[0] use index in list but not in dictionary 
dic['id'] = 120171122  # key = id, value = 120171122
dic['name'] = 'Ahmed'
dic['dept'] = 'MM'
dic['level'] = 1 
print(dic)

# In[37]:


print('id:', dic['id'])

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

# In[11]:


bag['money'] = 0
print(bag)


# In[8]:


bag['candy'] += 2
print(bag)


# In[9]:


print(bag['tissue'])


# In[10]:


print(bag['pen'])

# In[12]:


# if key in dictonary: 
if 'pen' in bag:
    print(bag['pen'])


# In[13]:


'pen' in bag

# In[14]:


# key in dictionary 
'candy' in bag

# In[15]:


# the value of the key 
bag['candy']

# In[16]:


# takes a key and return the value of the key
bag.get('pen')


# In[17]:


print(bag.get('pen'))


# In[18]:


# if key exists, retrurn the value, else return the default (0)
bag.get('pen', 0)


# In[19]:


# if key exists, retrurn the value, else return the default ('not found')
bag.get('pen', 'not found')


# In[20]:


bag.get('candy', 0)

# In[ ]:


bag.get('candy', 'not found')

# In[21]:


names = ['ahmed', 'mohammed', 'ali', 'hassan', 'khalid', 'ahmed', 'mohammed']
print(names)

# In[26]:


name_dict = dict()  # same as name_count = {}
for name in names:
    if name in name_dict:
        name_dict[name] += 1
    else:
        name_dict[name] = 1
    print(name_dict)
print('-------------------------')
print(name_dict)

# In[27]:


name_dict['ahmed']


# In[28]:


name_dict['khalid']

# In[29]:


# name_dict['mahmood']
name_dict.get('mahmood', 0)

# In[30]:


name_dict.get('mahmood', 'not found')

# In[31]:


# find name count using get 
name_dict = dict()  # same as name_count = {}
for name in names:
    # name_dict[name] += 1 in case name in the dict 
    # name_dict[name] = 0 + 1 in case name not in dict 
    name_dict[name] = name_dict.get(name, 0) + 1 
print(name_dict)

# In[32]:


name_dict.items()

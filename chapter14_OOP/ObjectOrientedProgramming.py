#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming in Python

# In[1]:


class PartyAnimal: # class name 
    # data
    x = 0

    # code
    def party(self):  
        self.x = self.x + 1 # class data 
        print("So far", self.x)


# In[2]:


l1  = list()  # define a list object 
d1  = dict()  # define a dictionary instance 
a1 = PartyAnimal() # define a PartyAnimal object / instance 


# In[3]:


l1.append(3)
a1.party() # make party 


# In[4]:


a1.party() # make party again :) 


# In[5]:


a1.party() # one more time :)


# In[6]:


a2 = PartyAnimal() # define another instance 
a2.party()


# # Local varaibles in functions 

# In[7]:


def f1():
    x = 10 
    print('x =', x)


# In[8]:


f1()


# In[9]:


print('x =', x) # name error. The scope of x is within the function 


# # The meaning of def party(self):

# In[10]:


a1.party()
PartyAnimal.party(a1) # the same 


# In[11]:


print(type(l1))
print(type(a1))


# In[12]:


print(dir(a1))


# # Access class field 

# In[13]:


a1.x


# In[14]:


a1.x = 10


# In[15]:


a1.x


# # Constructor / Destructor 

# In[16]:


class PartyAnimal:
   x = 0

   def __init__(self): # constractor # init = initilize 
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self): # destractor 
     print('I am destructed', self.x)


# In[17]:


a1 = PartyAnimal() # define object 


# In[18]:


a1.party()


# To see the destructor, we define an object within a scope of a function

# In[19]:


def f1():
    a = PartyAnimal()


# In[20]:


f1()
print('done')


# # Initialize object with constructor 

# In[21]:


class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)       


# In[22]:


# define list object and with initial values
l1 = list([1,2,3])
print(l1)


# In[23]:


# similarly
d = PartyAnimal("Dinsor")
h = PartyAnimal("Horse")


# In[24]:


d.party()
h.party()
d.party()


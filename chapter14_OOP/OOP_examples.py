#!/usr/bin/env python
# coding: utf-8

# # Class Examples in Python 

# ## Person

# In[1]:


class Person:
    name = ''
    gender = ''
    age = 0 
    def __init__(self, n, g, a):
        self.name = n
        self.age = a
        self.gender = g
    def walk(self):
        print('I am walking')
    def eat(self):
        print('I am eating :)')
    def __str__(self):
        return self.name


# In[2]:


p1 = Person('Ahmed', 'm', 20)
p2 = Person('Sally', 'f', 18)


# In[3]:


p1.walk()
p2.eat()


# In[4]:


print(p1)
print(p2)


# ## Circle
# ![image.png](attachment:image.png)
# 
# ---
# 
# ![image.png](attachment:image.png)

# In[5]:


class Circle:
    center = (0,0)
    radius = 0
    def __init__(self, c, r):
        self.center = c 
        self.radius = r 
    def get_aria(self):
        return self.radius * self.radius * 3.14
    def get_perimeter(self):
        return 2 * self.radius * 3.14 
    def __str__(self):
        return 'center: {}\traduis:{}'.format(self.center, self.radius)


# In[6]:


c1 = Circle((3,4), 2)
c2 = Circle((5,7), 9)


# In[7]:


c1.get_aria()


# In[8]:


c2.get_perimeter()


# ## Rectangle
# 
# ![image.png](attachment:image.png)
# 
# ---
# 
# ![image.png](attachment:image.png)

# ## Car 

# ## Book

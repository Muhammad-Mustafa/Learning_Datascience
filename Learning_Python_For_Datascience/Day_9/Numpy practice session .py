#!/usr/bin/env python
# coding: utf-8

# # Numpy Session

# In[1]:


pip install numpy


# In[2]:


#importing numpy

import numpy as np


# # Creating an array 

# In[3]:


#1-D Array

fruits = np.array(['Apple', 'Banana', 'Orange'])
fruits


# In[4]:


price = np.array([5,5,5])
price


# In[5]:


type(fruits)


# In[6]:


type(price)


# In[7]:


len(fruits)


# In[8]:


len(price)


# In[9]:


fruits[0:]


# In[10]:


price.mean()


# In[11]:


np.zeros(6)


# In[12]:


np.ones(5)


# In[13]:


np.empty(5)


# In[14]:


np.arange(10)


# In[15]:


np.arange(2,20)


# In[16]:


np.arange(2,20,1.2)


# In[17]:


#line space

np.linspace(1,10, num= 5)


# In[18]:


np.ones(3, dtype=np.int8)


# In[19]:


np.ones(3, dtype=np.float64)


# # Array Functions

# In[20]:


a = np.array([22,56,32,65,1,84,3,21,56,1,0])
a


# In[21]:


a.sort()


# In[22]:


a


# In[23]:


b = np.array([22.0,66.3,11.2,44.5,77,1,0.0,4])
b


# In[24]:


c = np.concatenate((a,b))
c


# In[25]:


c.sort()


# In[26]:


c


# In[48]:


#3-D array

a = np.array([
    [[1,2,3],
     [3,4,3]],
    
    [[5,6,3],
     [7,8,3]],
    
    [[9,10,3],
     [11,12,3]]
])
a


# In[45]:


a.size


# In[46]:


a.shape


# In[39]:


#how to find the dimentions 
a.ndim


# In[41]:


a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
a


# In[42]:


a.ndim


# In[43]:


a.shape


# In[53]:


a= np.arange(10)
a


# In[57]:


a.reshape(1,10)


# In[59]:


a = np.arange(9)
a


# In[60]:


a.shape


# In[61]:


a.ndim


# In[62]:


a.size


# In[63]:


a = a[np.newaxis, : ]
a


# In[64]:


a.ndim


# In[65]:


a.shape


# In[66]:


a.size


# In[67]:


a.reshape(3,3)


# In[68]:


a = np.arange(10)
a


# In[69]:


a*2


# In[70]:


a+2


# In[71]:


a-2


# In[72]:


a/2


# In[73]:


a.sum()


# In[74]:


a.mean()


# In[ ]:





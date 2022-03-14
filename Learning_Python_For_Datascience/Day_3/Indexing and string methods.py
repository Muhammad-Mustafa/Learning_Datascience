#!/usr/bin/env python
# coding: utf-8

# #  -- Indexing

# In[1]:


#make a string

a = "Muhammad Mustafa"
a


# In[5]:


#to find the lenght of the string

len(a)


# In[2]:


a[1]


# In[3]:


a[0]


# In[4]:


a[3]


# In[6]:


a[16]


# In[8]:


#the total length of the string is 16 but because the indexing is starting 
#form 0 so if you want to get the last element we have to write 15

a[15]


# In[11]:


#to print a range of indexing we can use loops but python also have a simple way to print
#the ranges using [0:8] the 0 is the starting index means that the values will start from 
# 0 index and also start printing from 0 index, but the index 8 shows that the value ends 
# at index 8 but do not print the value of that index because the last index in exclusive 

a[0:8]


# In[17]:


a[-10: -7]


# In[18]:


food = "Baryani"
food


# In[19]:


len(food)


# In[21]:


food.capitalize()


# In[23]:


food.lower()


# In[24]:


food.upper()


# In[31]:


food.replace('Bar', "Jani")


# In[26]:


name = "Hello my name is Muhammad Mustafa and I am a Datascientest"
name


# In[29]:


name.count('m')


# In[30]:


name.count('M')


# In[32]:


name.find('Mus')


# In[33]:


name.find('m')


# In[34]:


name.find('M')


# In[35]:


name.split(' ')


# In[ ]:





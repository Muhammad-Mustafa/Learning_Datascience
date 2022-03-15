#!/usr/bin/env python
# coding: utf-8

# # Basic Data Structure In Python
# 
# ## 1- Tuple
# ## 2- List
# ## 3- Dict
# ## 4- Set

# ## Tuple
# 
# **- ordered collection of elements**
# 
# **- enclosed with round braces ()**
# 
# **- Tuples are immutable means ones the values are entered, you cannot change the values**
# 

# In[1]:


#Tuples can store different data types 

#Basic Example
tup1 = (1, "Python", True, 2.5,1, "Python", True, 2.5)
tup1


# In[2]:


#Advance Example
tup2 = (1, "Python", True, 2.5,("Python", True, 2.5), ["Python", True, 2.5], {"name": "Mustafa"} )
tup2


# In[3]:


tup1[1]


# In[4]:


tup2[1:6]


# In[5]:


len(tup2)


# In[6]:


#Concatination
tup1 + tup2


# In[7]:


#Repetition
tup1*3


# In[8]:


tup3 = (10,20,30,40,50,60)
tup3


# In[9]:


min(tup3)


# In[10]:


max(tup3)


# In[11]:


type(tup2)


# In[12]:


tup1


# In[13]:


tup1.index('Python')


# In[14]:


#Count method will return the count how many time the given value appares in the dataType
tup1.count(2.5)


# ## List
# 
# **- ordered collection of elements**
# 
# **- enclosed with square braces []**
# 
# **- List are mutable means ones the values are entered, you can change the values**
#  

# In[15]:


#Simple Example
list1 = [1, 'Python', 2.5, "Mustafa",False, 66]
list1


# In[16]:


#Advance Example
adList = [1,"Mustafa", True, 9.0, (True, 33, 'Muhammad'),[True, 33, 'Muhammad'],{'name': "Mustafa"}]
adList


# In[17]:


list2 = [55, True, 33, 'Muhammad']
list2


# In[18]:


type(list1)


# In[19]:


len(list1)


# In[20]:


list1[2]


# In[21]:


#Concatination
list1 + list2


# In[22]:


list1 * 2


# In[26]:


list1.reverse()
list1


# In[28]:


list1.append("Hello")
list1


# In[29]:


list1.count("Hello")


# In[32]:


x = list1.copy()
x


# In[33]:


list1.clear()
list1


# In[34]:


list1 = x.copy()
list1


# In[35]:


list1.extend(x)
list1


# In[36]:


list1.count("Hello")


# In[37]:


list1.index('Mustafa')


# In[41]:


list1.insert(0,'newVal')
list1


# In[43]:


list1.pop()
list1


# In[44]:


list1.remove('newVal')
list1


# In[46]:


numList = [22,331,1,32,44,12,45,1,2,4,66,4,111,53,25,6,4,2,67,32,2,6,3,4,2165,45]
numList


# In[47]:


numList.sort()
numList


# ## Dict
# 
# **- unordered collection of elements**
# 
# **- enclosed with curly braces {}**
# 
# **- Dict are mutable means ones the values are entered, you can change the values**
#  
# **- Dict are consist of key value pairs** 

# In[51]:


dict1 = {"Name": "Mustafa", 'car': 'bmw'}
dict1


# In[52]:


#advance Dict
dict2 = {"Fruits_Prices":{'apple': 20, 'banana': 20}, "List_Of_Shops":[22,3,4,5,3,2,2]}
dict2


# In[57]:


y =  dict1.copy()
y


# In[59]:


dict1.clear()
dict1


# In[60]:


dict1 = y.copy()
dict1


# In[63]:


dict1.get('Name')


# In[64]:


dict1.items()


# In[65]:


dict1.keys()


# In[67]:


dict1.pop('car')
dict1


# In[71]:


dict1 = y.copy()


# In[72]:


dict1.popitem()


# In[73]:


dict1 = y.copy()


# In[74]:


dict1.update({'Room': 1})
dict1


# In[75]:


dict1.values()


# In[79]:


dict1.setdefault("Name","Muhammad")
dict1


# ## Sets
# 
# **- unordered collection of elements**
# 
# **- enclosed with curly braces {}**
# 
# **- unindexed**
#  
# **- no duplicates allowed** 

# In[80]:


set1 = {11,'Muhammad', "Mustafa", 33.33}
set1


# In[81]:


set1.add('newValue')
set1


# In[82]:


set2 = set1.copy()
set2


# In[83]:


set1.clear()
set1


# In[84]:


set1 = set2.copy()
set1


# In[89]:


abc_Set = {'a','b','c'}
abcd_Set = {'a','b','d'}


# In[90]:


#checks the 2 same length Sets and return the difference of the set

deff_set = abc_Set.difference(abcd_Set)
deff_set


# In[92]:


print(abc_Set.difference_update(abcd_Set))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





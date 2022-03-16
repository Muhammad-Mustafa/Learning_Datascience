#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[ ]:


username = input('Please enter your name: ')
weight = float(input('Please enter you weight in Kgs: '))
height = float(input('Please enter your height in meters: '))

def BMI_Calculator(weight, height):
    return weight/height**2

BMI = BMI_Calculator(weight, height)

print(username,'your BMI is ', BMI)


# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = 'ticks', color_codes = True)

titanic = sns.load_dataset('titanic')

sns.catplot(x = 'sex', y = 'survived', hue = 'class', kind = 'bar', data = titanic)
plt.show()


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = 'ticks', color_codes = True)

titanic = sns.load_dataset('titanic')

p1 = sns.catplot(x = 'sex', y = 'survived', hue = 'class', kind = 'bar', data = titanic)

p1.set_title = ('Plot for counting')
plt.show()


# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = 'ticks', color_codes = True)

titanic = sns.load_dataset('titanic')

plt2 = sns.FacetGrid(titanic, row = 'sex', hue = 'alone')
plt2 = (plt2.map(plt.scatter, 'age', 'fare').add_legend())
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





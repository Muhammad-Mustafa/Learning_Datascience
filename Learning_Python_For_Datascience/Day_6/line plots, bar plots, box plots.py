#!/usr/bin/env python
# coding: utf-8

# # Line Plot

# In[1]:


#import libraries 

import seaborn as sns
import matplotlib.pyplot as plt

#load dataset 

flowers = sns.load_dataset('iris')
print(flowers)


# In[2]:


#import libraries 

import seaborn as sns
import matplotlib.pyplot as plt

#load dataset 

flowers = sns.load_dataset('iris')

sns.lineplot(x = 'sepal_length', y = 'sepal_width', data = flowers)
plt.show()


# In[3]:


#import libraries 

import seaborn as sns
import matplotlib.pyplot as plt

#load dataset 

flowers = sns.load_dataset('iris')

#create the plot
sns.lineplot(x = 'sepal_length', y = 'sepal_width', data = flowers)

#setting the title of the plot
plt.title('Plot of flowers')

#adding the limit of axis 

plt.xlim(4)
plt.ylim(2)

plt.show()


# In[41]:


#import libraries 

import seaborn as sns
import matplotlib.pyplot as plt

#removing the style of the plot


#load dataset 

flowers = sns.load_dataset('iris')

#create the plot
sns.lineplot(x = 'sepal_length', y = 'sepal_width', data = flowers)

#setting the title of the plot
plt.title('Plot of flowers')

#adding the limit of axis 

plt.xlim(4)
plt.ylim(2)

#setting the styling of the plots
#white, dark, whitegrid, darkgrid, ticks
sns.set_style(style='darkgrid')
sns.set_style(style = None, rc = None)

plt.show()


# In[40]:


#import libraries 

import seaborn as sns
import matplotlib.pyplot as plt

#removing the style of the plot


#load dataset 

flowers = sns.load_dataset('iris')

#setting the figure size

plt.figure(figsize=(8,4))

#create the plot
sns.lineplot(x = 'sepal_length', y = 'sepal_width', data = flowers)

#setting the title of the plot
plt.title('Plot of flowers')

#adding the limit of axis 

plt.xlim(4)
plt.ylim(2)

#setting the styling of the plots
#white, dark, whitegrid, darkgrid, ticks
sns.set_style(style='darkgrid')
sns.set_style(style = None, rc = None)

plt.show()


# # Bar plot
# 

# In[16]:


#import libraries 

import seaborn as sns
import matplotlib.pyplot as plt

#load dataset 

flowers = sns.load_dataset('iris')
print(flowers)


# In[23]:


#import libraries 

import seaborn as sns
import matplotlib.pyplot as plt

#load dataset 

flowers = sns.load_dataset('iris')

#changing the figure

plt.figure(figsize=(8,4))

#creating the barplot

sns.barplot(x='species', y = 'sepal_width' ,data = flowers)

plt.show()


# In[24]:


#importing libraries 
import seaborn as sns
import matplotlib.pyplot as plt

titanic_ship_dataset =  sns.load_dataset('titanic')
print(titanic_ship_dataset)


# In[42]:


import seaborn as sns 
import matplotlib.pyplot as plt
from numpy import mean
titanic_dataset = sns.load_dataset('titanic')

plt.title('Titanic ship data')

sns.barplot(x ='sex', y = 'age', hue='alive' ,data = titanic_dataset, order=['female', 'male'], ci = None, estimator=mean)

sns.set_style('darkgrid')
sns.set_style(style=None, rc = None)

plt.show()


# In[43]:


import seaborn as sns 
import matplotlib.pyplot as plt
from numpy import mean
titanic_dataset = sns.load_dataset('titanic')

plt.title('Titanic ship data')

sns.barplot(x ='age', y = 'sex', hue='alive' ,data = titanic_dataset, order=['female', 'male'], ci = None, estimator=mean)

sns.set_style('darkgrid')
sns.set_style(style=None, rc = None)

plt.show()


# # Box plot

# In[50]:


import seaborn as sns 

tips_data = sns.load_dataset('tips')
tips_data.describe()


# In[53]:


import seaborn as sns 
import matplotlib.pyplot as plt
tips_data = sns.load_dataset('tips')

sns.boxplot(x='sex', y='tip', data=tips_data, hue='smoker', dodge=True)
plt.show()


# In[59]:


import seaborn as sns 
import matplotlib.pyplot as plt
tips_data = sns.load_dataset('tips')

sns.boxplot(x='tip', y='sex', data=tips_data, hue='smoker', dodge=True)
plt.show()


# In[60]:


import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


titanic_data = sns.load_dataset('titanic')
titanic_data.head()


# In[72]:


import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


titanic_data = sns.load_dataset('titanic')

p1 = sns.boxplot(x='sex', 
                 y='age', 
                 data = titanic_data, 
                 showmeans = True, 
                 meanprops = {
                     'marker': '*',
                     'markersize' : '12',
                     'markeredgecolor': 'red'
                 }
                )
plt.title('Ages of people in the titanic ship', size = '18')
plt.xlabel('Gender', size = '12')
plt.ylabel('Age', size = '12')


# In[ ]:





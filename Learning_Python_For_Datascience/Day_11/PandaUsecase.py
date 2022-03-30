# %% [markdown]
# # Case study (Pandas)
# 
# > Using Titanic dataset from Seaborn library

# %%
#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyt 
import seaborn as sns


# %%
#getting the dataset and storing it in a variable

titanic_ship_dataset = sns.load_dataset('titanic')
titanic_ship_dataset.head(3)

# %%
#saving dataframe into csv

titanic_ship_dataset.to_csv('titanic_dataset.csv')

# %%
#basic statistics and summary

titanic_ship_dataset.describe()

# %%
titanic_ship_dataset.head(3)

# %%
#droping columns from the dataset

titanic_ship_dataset.drop(['deck', 'embark_town', 'alone'],axis=1)


# %%
titanic_ship_dataset.mean()

# %%
titanic_ship_dataset.groupby(['sex', 'class']).mean()

# %%
titanic_ship_dataset.value_counts('survived')

# %%
# as we can see that the number of females are very high in survival rate lets see if that the number of childrens are
titanic_ship_dataset[titanic_ship_dataset['age'] < 18].mean()

# %%
#now we can see how many childrens were survived

titanic_ship_dataset[titanic_ship_dataset['age'] < 18].groupby(['sex', 'class']).mean()

# %%
print(titanic_ship_dataset['age'].mode())

# %%
#importing the Pakistan hunger and food insecurity

PK_HFI = pd.read_csv('hunger and food insecuirty Pakistan dataset.csv')


# %%
PK_HFI.head()

# %%
PK_HFI.describe()

# %%




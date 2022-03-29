# %%
import pandas as pd
import numpy as np

# %%
#Objection Creation 
s= pd.Series([1,2,3,4,np.nan,4,3,2])
s

# %%
dates = pd.date_range('20130101',periods=6)
dates

# %%
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df

# %%
np.random.randn(6,4)

# %%
df2 = pd.DataFrame(
  {
    "A":1.0,
    "B":pd.Timestamp('20220202'),
    "C":pd.Series(1,index=list(range(4)), dtype='float32'),
    "D":np.array([3,3,3,3], dtype='int32'),
    "E":pd.Categorical(['test', 'train','test', 'train']),
    "F":'foo'
  }
)

df2

# %%
df2.dtypes

# %%
df2.head(2)

# %%

df2.tail(2)

# %%
df2.index

# %%
convert_datafrom_to_array = df2.to_numpy()
convert_datafrom_to_array

# %%
df2.describe()

# %%
df2.T

# %%




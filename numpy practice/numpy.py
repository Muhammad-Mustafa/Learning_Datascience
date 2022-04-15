# %% [markdown]
# # Learning Numpy Library and practise

# %%
import numpy as np 


# %% [markdown]
# # Basics

# %%
One_DArray  =  np.array([12,3,4,3,5,3], dtype='float16')
One_DArray


# %%
Two_DArray = np.array([[4.0,5.0,7.0],[4.0,5.0,7.0], [4.0,5.0,3.0],[4.0,5.0,3.0]])
Two_DArray

# %%
Three_DArray = np.array([[[4.0,5.0,7.0],[4.0,5.0,7.0]],[[4.0,5.0,7.0],[4.0,5.0,7.0]],[[4.0,5.0,7.0],[4.0,5.0,7.0]],[[4.0,5.0,7.0],[4.0,5.0,7.0]],[[4.0,5.0,7.0],[4.0,5.0,7.0]]])
Three_DArray

# %%
# what type is that array 

print('Type of One_DArray : ', type(One_DArray))
print('Type of Two_DArray : ', type(Two_DArray))
print('Type of Three_DArray : ', type(Three_DArray))

# %%
# How to get the dimension of the array 
print('One_DArray.ndim : ',One_DArray.ndim)
print('Two_DArray.ndim : ',Two_DArray.ndim)
print('Three_DArray.ndim : ',Three_DArray.ndim)

# %%
# How to get the shape of the array 
print('One_DArray.shape : ',One_DArray.shape)
print('Two_DArray.shape : ',Two_DArray.shape)
print('Three_DArray.shape : ',Three_DArray.shape)

# %%
#how to get the type of the array 

print('One_DArray.dtype : ', One_DArray.dtype)
print('Two_DArray.dtype : ', Two_DArray.dtype)
print('Three_DArray.dtype : ', Three_DArray.dtype)

# %%
#print the size of the array 

print('One_DArray.size : ',One_DArray.size)
print('Two_DArray.size : ',Two_DArray.size)
print('Three_DArray.size : ',Three_DArray.size)

# %%
#print the size of the iteam array note the number is repersenting the size in bytes 

print('One_DArray.itemsize : ',One_DArray.itemsize)
print('Two_DArray.itemsize : ',Two_DArray.itemsize)
print('Three_DArray.itemsize : ',Three_DArray.itemsize)

# %% [markdown]
# # Accessing/Changing elements, rows, columns etc

# %%
arr1 = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
arr1

# %%
#get a specific element in this formate [row, column]
arr1[1, -2]

# %%
#get a specific row

arr1[1, :]

# %%
#get a specific column
arr1[:, 3]

# %%
#gettig a little more fancy [startIndex:endIndex:stepsize]

print(arr1[0, 1:6:2])
print(arr1[0, ::2])
print(arr1[0, 1::2])

# %%
arr1[1,-1] = 50
arr1

# %%
arr1[:,2] = 0
arr1

# %%
arr1[1,:] = 0
arr1

# %%
arr2 = np.array([
  [[1,2],[3,4]],
  [[5,6],[7,8]],
  [[9,10],[11,12]],
  [[13,14],[15,16]],
])
arr2

# %%
arr2[2,1,1]

# %%
arr2[:,:,0]

# %% [markdown]
# # Initializing all type of array 

# %%
# All 0's arrays

arr3 = np.zeros((3,))
arr3

# %%
np.ones(3, dtype='int32')

# %%
np.full((3,4), 45, dtype='int32')

# %%
#random values array

np.random.rand(4,2)

# %%
#np identity matrix

np.identity(4)

# %%
arr1 = np.ones((5,5))
arr1

# %%
arr2 = np.zeros((3,3))
arr2

# %%
arr2[1,1] = 9
arr2

# %%
arr1[1:-1, 1:-1] = arr2
arr1

# %%




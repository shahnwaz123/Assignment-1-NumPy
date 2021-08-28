#!/usr/bin/env python
# coding: utf-8

# # Assignment1-Numpy
# 

# In[1]:


import numpy as np


# # Q-1 Use numpy to generate array of 25 random numbers sampled from a standard normal distribution

# In[ ]:


rand_num = np.random.normal(0,1,25) print("25 random numbers from a standard normal distribution:") print(rand_num)


# # Q-2 Create a random vector of size 30 and find the mean value.

# In[ ]:


x = np.random.random(30) x.mean() print(x.mean())


# # Q3-Insert 1 to 100 numbers in a numpy array and reshape it to 10*10 matrix.

# In[ ]:


data1 = list(range(1, 101)) arr1 = np.array(data1) arr1 = np.arange(1, 101).reshape(10, -1) print(arr1)


# # Q4-Create a 10x10 array with random values and find the minimum and maximum values.

# In[ ]:


arr = np.random.random((10,10)) print("Original Array:") print(arr) arrmin, arrmax = arr.min(), arr.max() print("Minimum and Maximum Values:",arrmin, arrmax)


# # Q5-Find Dot product of two arrays

# In[ ]:


f = np.array([1,2]) g = np.array([4,5]) print(np.dot(f,g))


# # Q6-Concatenate following arrays along axis=0

# In[ ]:


x=np.array([[1,2],[3,4]]) y=np.array([[5,6]]) print(np.concatenate((x, y), axis=0))


# # Q7-How to get the common items between two python numpy arrays?

# In[ ]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8]) print(np.intersect1d(a,b))


# # Q8-Sort the numpy array:

# In[ ]:


arr = np.array([10,5,8,4,7,2,3,1]) print(np.sort(arr))


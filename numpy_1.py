#!/usr/bin/env python
# coding: utf-8

# ## Basics of Numpy 

# In[1]:


import numpy as np


# In[2]:


a=np.array([0,1,2,3,4])
print(a)


# In[3]:


a[0]


# In[4]:


a[0:]


# In[5]:


type(a)


# In[6]:


a[: :-1]


# In[30]:


A = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])

print(A[:, :2])


#  ## Dimension and shape and Size 

# In[8]:


A=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])


# In[9]:


A.dtype  #data type 


# In[10]:


A.shape  #for shape 


# In[11]:


A.size  #for size 


# In[12]:


A.ndim # for dimension


# ## Multiple Slicing 

# In[13]:


B=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])


# In[14]:


B[0,0]  #for first element of first row 


# In[15]:


B[2,3]


# In[17]:


B[: :-1]


# In[26]:


B[:2, :2]


# ## Formatting 

# In[27]:


B[0,0]=0


# In[28]:


B


# In[29]:


B[1,2]=3
B


# In[ ]:





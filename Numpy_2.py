#!/usr/bin/env python
# coding: utf-8

# ## Numpy Operationa 

# In[1]:


import numpy as np


# In[2]:


a=np.array(range(5))  #range function in numpy 
a


# In[3]:


a+5   #perform operation on array


# In[4]:


a


# In[5]:


x=a+10
x


# In[6]:


b=np.array(range(2,10))
b


# In[7]:


c=np.array(range(2,20,2))
c


# In[8]:


# adding two arrays 




d=np.array([1,2,3])
e=np.array([10,20,30])     #for this addition array should be same dimension
d+e                     







# ## Boolean Arrays

# In[12]:


A=np.array(range(6))
A


# In[21]:


B=A


# In[22]:


B


# In[23]:


B[0]


# In[26]:


B[[0,-1]]    #normal Indexing 


# In[27]:


B[[True,False,False,False,False,True]]    #Boolean Indexing


# In[33]:


B >=2   #advantage of boolean array easily sort numbers


# In[34]:


B[B >=2]


# In[35]:


B.mean()








#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
new_array=np.array([1,2,3])
new_list = new_array.tolist()
new_list


# In[11]:


array=np.eye(6)
trace = np.trace(array)
trace


# In[28]:


def min(a,x):
    variable=np.shape(a)
    n=variable[0]
    m=variable[1]
    for i in range(n):
            for j in range(m): 
                if a[i,j]>x:
                    print(a[i,j])
a = np.array([[1,2],[3,5],[7,8]])
x=2
min(a,x)


# In[20]:


A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
C=A+B
C


# In[29]:


def mean(a):
    variable=np.shape(a)
    n=variable[0]
    m=variable[1]
    S=0
    for i in range(n):
            for j in range(m): 
                S += a[i,j]
            Moyenne = S / m 
            print(Moyenne)
            S=0
                    
a = np.array([[1,2],[3,5],[7,8]])
mean(a)


# In[ ]:





# In[ ]:





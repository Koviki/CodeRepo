#!/usr/bin/env python
# coding: utf-8

# # plotting x,y

# In[1]:


import sklearn as sl


# In[2]:


import matplotlib.pyplot as plt


# In[4]:


x = [i for i in range(10)]
print (x)


# In[6]:


y = [2*i for i in range(10)]
print (y)


# In[7]:


plt.plot(x,y)


# In[8]:


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x,y)


# In[9]:


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.scatter(x,y)


# In[ ]:





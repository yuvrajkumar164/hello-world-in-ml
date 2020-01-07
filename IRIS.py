#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris=pd.read_csv("iris.csv")

iris


# In[49]:


print(iris.shape)


# In[50]:


print(iris.columns)


# In[51]:


iris["species"].value_counts()


# In[52]:


iris.plot(kind='scatter',x='sepal_length',y='sepal_width')
plt.show()


# In[53]:


sns.set_style("whitegrid")
sns.FacetGrid(iris, hue="species",height=4)    .map(plt.scatter, "sepal_length", "sepal_width")    .add_legend()
plt.show()


# In[55]:


plt.close()
sns.set_style("whitegrid");
sns.pairplot(iris,hue="species",height=3,diag_kind="kde")
plt.show()


# In[ ]:





# In[ ]:





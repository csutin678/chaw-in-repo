#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[10]:


df = pd.read_csv('UCL Final.csv')
df.head()


# In[11]:


df.isnull().sum()


# In[12]:


df.info()


# In[20]:


sns.set(rc={'figure.figsize':(18,9), 'lines.linewidth': 5, 'lines.markersize': 5, "axes.labelsize":15}, style="whitegrid")

best_team = df.club[df['position'] == 'winner'].value_counts()


# In[23]:


sns.barplot(x=best_team, y=best_team.index, data=df)


# In[24]:


most_team = df['club'].value_counts()


# In[25]:


sns.barplot(x=most_team, y=most_team.index, data=df)


# In[ ]:





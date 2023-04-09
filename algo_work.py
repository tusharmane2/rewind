#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("C:/Users/tushar.mane_embibe/Downloads/Daily Work Tracker_Project - Algo - Algo_DWT.csv")
df.head()


# In[6]:


grouped_df = df.groupby(['Name', 'Main Task'])[['Qty. of Work', 'Time spent (in hrs)']].sum()
grouped_df.head()


# In[7]:


grouped_df = grouped_df.reset_index()
grouped_df.head()


# In[51]:


efficiency = grouped_df['Qty. of Work']/grouped_df['Time spent (in hrs)']
grouped_df = grouped_df.assign(task_efficiency= efficiency)
grouped_df.head(50)


# In[52]:


# reset the index and pivot the table to make name the index and type of task the columns
pivoted_grouped_df = grouped_df.pivot(index='Name', columns='Main Task', values='task_efficiency')

# plot a bar chart for each name
pivoted_grouped_df.plot.bar()
plt.show()


# In[48]:


grouped_by_task = grouped_df.groupby('Main Task')

# create a separate bar graph for each task
for task, group in grouped_by_task:
    plt.figure()
    group.plot.bar(x='Name', y='task_efficiency')
    plt.title(f'Task {task}')
    plt.xlabel('Employee')
    plt.ylabel('Task efficiency')
    plt.show()


# In[ ]:





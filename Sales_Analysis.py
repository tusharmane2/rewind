#!/usr/bin/env python
# coding: utf-8

# In[116]:


import pandas as pd
import numpy as np


# In[117]:


import os


# Task 1 is to combine all the csv files into one dataframe

# In[118]:


location_string = "C:/Users/tushar.mane_embibe/Downloads/Pandas-Data-Science-Tasks-master/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data"
files = [file for file in os.listdir(location_string)]
for file in files:
    print(file)


# Create a empty dataset called all_months_data and use for loop to concatinate the files

# In[119]:


all_months_data = pd.DataFrame()
for file in files:
    df = pd.read_csv(location_string+'/'+file)
    all_months_data = pd.concat([all_months_data, df])
all_months_data.head()


# In[120]:


all_months_data.shape


# ### What was the best month for sales? What was the revenue that month?

# In[63]:


all_months_data['Quantity Ordered'].dtype


# In[121]:


all_months_data.dropna(inplace=True)
all_months_data.head()


# In[137]:


all_data = all_months_data[all_months_data['Order ID'] != 'Order ID']
all_data.dtypes


# In[138]:


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])


# In[139]:


all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


# In[140]:


all_data.dtypes


# In[141]:


all_data['Order Value'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# In[144]:


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])


# In[145]:


all_data.dtypes


# In[151]:


all_data['Order Month'] = all_data['Order Date'].dt.strftime('%B %Y')
print(all_data.dtypes)
all_data.head()


# In[134]:


all_data['Month Number'] = all_data['Order Date'].dt.month
all_data['Year'] = all_data['Order Date'].dt.year

# set financial year start and end months
start_month = 4
end_month = 3

# create a function to determine financial year
def get_financial_year(row):
    if row['Month Number'] >= start_month:
        return row['Year']
    else:
        return row['Year'] - 1

# apply the function to create 'Financial Year' column
all_data['Financial Year'] = all_data.apply(get_financial_year, axis=1)

# sort the dataframe by 'Financial Year' and 'Month Number' columns
all_data = all_data.sort_values(['Financial Year', 'Month Number'])

# drop the temporary columns
all_data = all_data.drop(['Month Number', 'Year', 'Financial Year'], axis=1)


# In[152]:


monthly_sale = all_data.groupby(['Order Month'])['Order Value'].sum()
monthly_sale


# In[ ]:





# In[155]:


import matplotlib.pyplot as plt
ax = monthly_sale.plot.bar()

# set the plot title and labels
ax.set_title('Monthly Sale')
ax.set_xlabel('Month')
ax.set_ylabel('Sale')

# display the plot
plt.show()


# ### What city has the highest sale?

# In[156]:


all_data.head()


# In[157]:


def get_city(address):
    # split the address string using comma separator
    address_parts = address.split(',')
    # the city name is the second element after splitting by comma
    city = address_parts[1].strip()
    return city

# apply the function to the 'Address' column and create a new column 'City'
all_data['City'] = all_data['Purchase Address'].apply(get_city)
all_data.head()


# In[159]:


city_sales = all_data.groupby('City')['Order Value'].sum()
city_sales


# In[160]:


ax = city_sales.plot.bar()

ax.set_title('City wise sales')
ax.set_xlabel('City')
ax.set_ylabel('Sales')

plt.show()


# In[ ]:





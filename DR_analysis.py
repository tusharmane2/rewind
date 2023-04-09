#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[111]:


df =  pd.read_csv("C:/Users/tushar.mane_embibe/Downloads/DR.csv")
df.head()


# In[113]:


sns.histplot(x = 'q1 feedback', data = df)
plt.xticks(rotation=30)


# In[117]:


df.describe(include = 'all')


# In[56]:


q1_counts = df['q1 feedback'].value_counts()
print(q1_counts)
# create the pie chart
plt.figure(figsize=(6,6))
plt.pie(q1_counts, labels=q1_counts.index, autopct='%1.1f%%')
plt.title('q1 feedback')


# In[57]:


q2_counts = df['q2 feedback'].value_counts()
plt.pie(q2_counts, labels = q2_counts.index, autopct = '%1.1f%%')
plt.title('Feedback of q2')


# In[58]:


high_sim = df.loc[df['q1 feedback'].isin(['Exact'])]['q1_sim'].gt(0.9).sum()
# this can also be found by high_sim = df[df['q1 feedback'] == 'Exact']['q1_sim'].gt(0.9).sum()
mid_sim = df.loc[df['q1 feedback'].isin(['Exact'])]['q1_sim'].between(0.8, 0.9).sum()
low_sim =df.loc[df['q1 feedback'].isin(['Exact'])]['q1_sim'].lt(0.8).sum()
high_sim+mid_sim+low_sim


# In[119]:


similarity_list = [high_sim, mid_sim, low_sim]

# create a list of labels for each count
labels = ['High', 'Mid', 'Low']

# create a pie chart from the counts and labels
plt.pie(similarity_list, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of similarity score for q1 with Exact result')


# In[59]:


q2high_sim = df.loc[df['q2 feedback'].isin(['Exact'])]['q1_sim'].gt(0.9).sum()
q2mid_sim = df.loc[df['q2 feedback'].isin(['Exact'])]['q1_sim'].between(0.8, 0.9).sum()
q2low_sim =df.loc[df['q2 feedback'].isin(['Exact'])]['q1_sim'].lt(0.8).sum()
q2high_sim+q2mid_sim+q2low_sim


# In[60]:


similarity_list = [q2high_sim, q2mid_sim, q2low_sim]

# create a list of labels for each count
labels = ['High', 'Mid', 'Low']

# create a pie chart from the counts and labels
plt.pie(similarity_list, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of similarity score for q2 with Exact result')


# In[9]:


similar_high_sim = df.loc[df['q1 feedback'].isin(['Similar'])]['q1_sim'].gt(0.9).sum()
similar_mid_sim = df.loc[df['q1 feedback'].isin(['Similar'])]['q1_sim'].between(0.8, 0.9).sum()
similar_low_sim =df.loc[df['q1 feedback'].isin(['Similar'])]['q1_sim'].lt(0.8).sum()
similarity_list = [similar_high_sim, similar_mid_sim, similar_low_sim]

# create a list of labels for each count
labels = ['High', 'Mid', 'Low']

# create a pie chart from the counts and labels
plt.pie(similarity_list, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of similarity score for q1 with Similar result')


# In[61]:


diff_high_sim = df.loc[df['q1 feedback'].isin(['Different'])]['q1_sim'].gt(0.9).sum()
# this can also be found by diff_high_sim = df[df['q1 feedback'] == 'Different']['q1_sim'].gt(0.9).sum()
diff_mid_sim = df.loc[df['q1 feedback'].isin(['Different'])]['q1_sim'].between(0.8, 0.9).sum()
diff_low_sim =df.loc[df['q1 feedback'].isin(['Different'])]['q1_sim'].lt(0.8).sum()
similarity_list = [diff_high_sim, diff_mid_sim, diff_low_sim]
# create a list of labels for each count
labels = ['High', 'Mid', 'Low']

# create a pie chart from the counts and labels
plt.pie(similarity_list, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of similarity score for q1 with Different result')


# In[62]:


value_counts_sub = df['question_subject'].value_counts()
value_counts_sub


# In[63]:


plt.pie(value_counts_sub, labels = value_counts_sub.index, autopct = '%1.1f%%')
plt.title('Distribution of subjects')


# In[64]:


filter_list = ['Exact', 'Similar', 'Different']
filter_list_sub = ['physics', 'chemistry', 'mathematics', 'science']
df_new = df.loc[df['q1 feedback'].isin(filter_list) & df['question_subject'].isin(filter_list_sub)]
df_new.head()


# In[124]:


grouped = df_new.groupby(['question_subject', 'q1 feedback']).size().reset_index(name = 'count')
print(grouped)

# Pivot the dataframe to make the categories into columns
pivoted = grouped.pivot(index='question_subject', columns='q1 feedback', values='count')
print(pivoted)

# Calculate the percentage distribution for each subject
total_counts = pivoted.sum(axis=1)
percentage_distribution = pivoted.divide(total_counts, axis=0)*100

# Plot the bar graph
ax = percentage_distribution.plot(kind='bar', stacked=True)
ax.set_ylabel('Percentage')
ax.set_xlabel('Subject')
ax.set_title('Subjectwise feedback distribution of q1')


# In[66]:


# create a pivot table with subjects as rows and results as columns
pivot = grouped.pivot(index='question_subject', columns='q1 feedback', values='count')

print(pivot)
# create a bar chart of the pivot table
pivot.plot(kind='bar', stacked = True)

# set the chart title and axis labels
plt.title('Results by Subject')
plt.xlabel('Subject')
plt.ylabel('Count')


# In[67]:


value_counts_phy = df_new[df_new['question_subject'] == 'physics']['q1 feedback'].value_counts()
value_counts_phy


# In[68]:


plt.pie(value_counts_phy, labels = value_counts_phy.index, autopct = '%1.1f%%')
plt.title('Feedback of Physics for q1')


# In[69]:


value_counts_maths = df_new[df_new['question_subject'] == 'mathematics']['q1 feedback'].value_counts()
plt.pie(value_counts_maths, labels = value_counts_maths.index, autopct = '%1.1f%%')
plt.title('Feedback of Mathematics')


# In[70]:


value_counts_chem = df_new[df_new['question_subject'] == 'chemistry']['q1 feedback'].value_counts()
plt.pie(value_counts_chem, labels = value_counts_chem.index, autopct = '%1.1f%%')
plt.title('Feedback of Chemistry')


# In[71]:


value_counts_sci = df_new[df_new['question_subject'] == 'science']['q1 feedback'].value_counts()
plt.pie(value_counts_sci, labels = value_counts_sci.index, autopct = '%1.1f%%')
plt.title('Feedback of Science')


# In[75]:


df_new.head()


# In[80]:


grouped_data = df_new.groupby(['question_subject', 'q1 feedback'])

group_data = grouped_data.get_group(('physics', 'Exact'))

# Select the columns for the box plot
boxplot_data = group_data[['question_subject', 'q1 feedback', 'q1_sim']]

# Create the box plot
boxplot_data.boxplot()
plt.title("Box plot for 'physics' and 'Exact'")
plt.xlabel("Column Names")
plt.ylabel("Values")
plt.show()


# In[83]:


for group_name, group_data in grouped_data:
    boxplot_data = group_data[['question_subject', 'q1 feedback', 'q1_sim']]
    print(group_name)
    print(boxplot_data)
    boxplot_data.boxplot()
    plt.title(f"Box plot for {group_name}")
    plt.xlabel("Column Names")
    plt.ylabel("Values")
    plt.show()


# In[102]:


# create bins for the values of q1_sim
bins = [0, 0.8, 0.9, 1]

# create labels for the categories
labels = ['Low', 'Mid', 'High']

# create the new column 'q1_sim_category' based on the bins and labels
df_new['q1_sim_category'] = pd.cut(df_new['q1_sim'], bins=bins, labels=labels, include_lowest=True)


# In[145]:


# group the data by 'question_subject' and 'q1 feedback', and count the number of values in each category of 'q1_sim_category'
grouped_data = df_new.groupby(['question_subject', 'q1 feedback', 'q1_sim_category']).size().reset_index(name='count')


# In[146]:


grouped_data.head()


# In[107]:


# loop over the unique values of 'question_subject' and 'q1 feedback', and create a pie chart for each combination
for subj in df_new['question_subject'].unique():
    for feedback in df_new['q1 feedback'].unique():
        
        # filter the grouped data for the current combination of 'question_subject' and 'q1 feedback'
        filt = (grouped_data['question_subject'] == subj) & (grouped_data['q1 feedback'] == feedback)
        data = grouped_data.loc[filt, :]
        
        # create the pie chart
        plt.figure()
        plt.pie(data['count'], labels=data['q1_sim_category'], autopct = '%1.1f%%')
        plt.title(f"{subj} - {feedback}")
        plt.show()


# In[128]:


grouped_data = df_new.groupby(['question_subject', 'q1 feedback', 'q1_sim_category']).size().reset_index(name='count')
for subject in grouped_data['question_subject'].unique():
    data = grouped_data[grouped_data['question_subject']==subject].set_index(['q1 feedback', 'q1_sim_category'])
    data['count'].unstack().plot(kind='bar', stacked=True)
    plt.title(f'{subject}')
    plt.show()


# In[129]:


pivoted_data = grouped_data.pivot(index='question_subject', columns=['q1 feedback', 'q1_sim_category'], values='count')
sns.heatmap(pivoted_data, cmap='YlGnBu')
plt.show()


# In[130]:


plt.stackplot(pivoted_data.index, pivoted_data['Exact']['High'], pivoted_data['Similar']['High'], pivoted_data['Different']['High'], labels=['Exact', 'Similar', 'Different'])
plt.legend(loc='upper left')
plt.show()


# In[131]:


sns.violinplot(x='q1 feedback', y='q1_sim', hue='q1_sim_category', data=df_new)
plt.show()


# In[133]:


df_new.boxplot(column='q1_sim', by='question_subject')
plt.show()


# In[136]:


get_ipython().system('pip install wordcloud')


# In[137]:


from wordcloud import WordCloud

wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_text(' '.join(df_new['question_subject'].astype(str)))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[150]:





# In[149]:





# In[ ]:





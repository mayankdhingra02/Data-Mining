#!/usr/bin/env python
# coding: utf-8

# In[1]:


import charts
from matplotlib import pyplot


# In[6]:


years= [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
gdp = [14964.37, 15517.93, 16155.26, 16691.52, 17427.61, 18120.71, 18624.48, 19390.6]

def line_chart():
    pyplot.plot(years, gdp, color='green', marker='o', linestyle='solid')
    pyplot.title("Nominal GDP of United States")
    pyplot.ylabel("$ in Billions")
    pyplot.show()


# In[7]:


line_chart()


# In[8]:


def bar_chart():
    pyplot.bar(years, gdp)
    pyplot.title("Nominal GDP of United States")
    pyplot.ylabel("$ in Billions")
    pyplot.show()


# In[9]:


bar_chart()


# In[20]:


users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]


# In[21]:


count=0
for i in range(0,len(users)):
    count=0
    for j in range(0,len(friendship)):
        if(users[i]["id"]==friendship[j][0] or users[i]["id"]==friendship[j][1]):
            count+=1
    users[i]['friends']=count


# In[22]:


def num_friends(user):
    count=0
    for i in range(0,len(friendship)):
        if(user["id"]==friendship[i][0] or user["id"]==friendship[i][1]):
            count+=1
    return count


# In[23]:


user={"id":3}
num_friends(user)


# In[24]:


def return_key(elem):
    return elem["friends"]


# In[25]:


def sort_by_num_friends():
    users.sort(reverse=True, key=return_key)


# In[26]:


users


# In[27]:


sort_by_num_friends()


# In[28]:


users


# In[ ]:





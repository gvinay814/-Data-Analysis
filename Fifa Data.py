#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
fifa=pd.read_csv(r"C:\Users\VINAY KUMAR\Downloads\players_20.csv\players_20.csv")


# In[4]:


fifa.head()


# In[5]:


for col in fifa.columns:
    print(col)


# In[7]:


fifa.shape


# In[10]:


fifa['nationality'].value_counts()[0:5].keys()


# In[16]:


nationality_name=list(fifa['nationality'].value_counts()[0:5].keys())
nationality_count=list(fifa['nationality'].value_counts()[0:5])
plt.bar(nationality_name,nationality_count,color='red')
plt.show()


# In[18]:


players_salary=fifa[['short_name','wage_eur']]


# In[19]:


players_salary.head()


# In[21]:


players_salary=players_salary.sort_values(by=['wage_eur'],ascending=False)


# In[26]:


ply_name=list(players_salary['short_name'][0:5])
ply_salary=list(players_salary['wage_eur'][0:5])
plt.bar(ply_name,ply_salary)


# In[27]:


fifa['nationality']=='Germany'


# In[28]:


Germany=fifa[fifa['nationality']=='Germany']
Germany.head()


# In[29]:


Germany.sort_values(by=['weight_kg'],ascending=False)


# In[30]:


Germany.sort_values(by=['height_cm'],ascending=False).head()


# In[ ]:





# In[31]:


Germany.sort_values(by=['wage_eur'],ascending=False).head()


# In[32]:


Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()


# In[34]:


players_shooting=fifa[['short_name','shooting']]


# In[37]:


players_shooting.sort_values(by=['shooting'],ascending=False).head()


# In[38]:


#defending rating


# In[40]:


players_defending=fifa[['short_name','defending']]
players_defending.sort_values(by=['defending'],ascending=False).head()


# In[43]:


india=fifa[fifa['nationality']=='India']


# In[44]:


india.head()


# In[58]:


sunil=india[india['height_cm']=='170']


# In[53]:


sunil.head()


# In[ ]:


players


# In[54]:


india.sort_values(by=['wage_eur'],ascending=False).head()


# In[55]:


india.sort_values(by=['shooting'],ascending=False).head()


# In[57]:


india['nationality'].value_counts()


# In[59]:


sunil=india[india['height_cm']=='170']
sunil.head()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
ipl=pd.read_csv(r'C:\Users\VINAY KUMAR\Downloads\matches.csv')
ipl.head()


# In[ ]:





# In[ ]:





# In[21]:


ipl.tail()


# In[6]:


ipl['player_of_match'].value_counts()[0:5]


# In[16]:


top5=list(ipl['player_of_match'].value_counts()[0:5].keys())
top5val=list(ipl['player_of_match'].value_counts()[0:5])
print(top5val)


# In[18]:


from matplotlib import pyplot as plt
plt.bar(top5,top5val,color='cyan')
plt.show()


# In[19]:


ipl['result'].value_counts()


# In[20]:


ipl['toss_winner'].value_counts()


# In[22]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[23]:


batting_first.head()


# In[25]:


top3batting_first_winners=list(batting_first['winner'].value_counts()[0:3].keys())
top3batting_first_winners_val=list(batting_first['winner'].value_counts()[0:3])


# In[27]:


batting_second=ipl[ipl['win_by_wickets']!=0]


# In[28]:


batting_second.head()


# In[30]:


batting_second['winner'].value_counts()


# In[31]:


plt.hist(batting_first['win_by_runs'])
plt.title("distribution of runs")
plt.xlabel("win by runs")
plt.show()


# In[54]:


plt.hist(batting_second['win_by_wickets'],bins=40)
plt.title("distribution of wickets")
plt.xlabel("win by wickets")
plt.show()


# In[44]:


top3batting_first_winners=list(batting_first['winner'].value_counts()[0:3].keys())
top3batting_first_winners_val=list(batting_first['winner'].value_counts()[0:3])

plt.bar(top3batting_first_winners,top3batting_first_winners_val,color=["blue","yellow",'orange'])


# In[43]:


top5_batting_second_winners=list(batting_second['winner'].value_counts()[0:5].keys())
top5_batting_second_winners_vals=list(batting_second['winner'].value_counts()[0:5])
plt.figure(figsize=(20,4))

plt.bar(top5_batting_second_winners,top5_batting_second_winners_vals,color=["purple","blue","red","yellow","pink"])


# In[52]:


name_of_team=list(batting_first['winner'].value_counts().keys())
no_of_wins=list(batting_first['winner'].value_counts())
plt.pie(no_of_wins,labels=name_of_team,autopct='%0.1f%%')


# In[55]:


ipl['season'].value_counts()


# In[56]:


ipl['city'].value_counts()


# In[59]:


import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[60]:


deliveries=pd.read_csv(r"C:\Users\VINAY KUMAR\Downloads\deliveries.csv\deliveries.csv")


# In[64]:


deliveries.head()


# In[62]:


deliveries['match_id'].unique()


# In[65]:


match1=deliveries[deliveries['match_id']==1]


# In[66]:


match1.tail()


# In[68]:


srh=match1[match1['inning']==1]


# In[69]:


srh.tail()


# In[70]:


srh['batsman_runs'].value_counts()

srh['dismissal_kind
# 

# In[71]:


srh['dismissal_kind'].value_counts()


# In[73]:


rcb=match1[match1['inning']==2]


# In[74]:


rcb.tail()


# In[75]:


rcb['batsman_runs'].value_counts()


# In[77]:


rcb['dismissal_kind'].value_counts()


# In[ ]:





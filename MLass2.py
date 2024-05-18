# ## DATASET 1

# In[1]:


import pandas as pd

data = pd.read_csv("C:\\Users\\HP\\Downloads\\placement - placement.csv")
data


# In[2]:


data.head()


# In[3]:


data.tail()


# In[4]:


data.sample(15)


# In[5]:


data.describe()


# In[6]:


data.info()


# In[7]:


data['placed'][3] = 0 
data.head()


# In[8]:


data.loc[2:25, ['cgpa', 'resume_score']]


# In[9]:


data.iloc[2:14, 1:3]


# In[10]:


data['cgpa'][0] = None
data


# In[11]:


data['resume_score'][4] = None
data



# In[12]:


data.isnull()


# In[13]:


data.isnull().sum()


# In[14]:


data.dropna()


# ## DATASET 2

# In[15]:


data2 = pd.read_csv("C:\\Users\\HP\Downloads\\insurance - insurance.csv")
data2


# In[16]:


data2.head()


# In[17]:


data2.tail()


# In[18]:


data2.sample(15)


# In[19]:


data2.describe()


# In[20]:


data2.info()


# In[21]:


data2.loc[2:25, ['age', 'sex']]


# In[22]:


data2.iloc[2:14, 1:3]


# In[23]:


data2['age'][0] = None
data2


# In[24]:


data2['sex'][4] = None
data2



# In[25]:


data2.isnull()


# In[26]:


data2.dropna()


# ## DATASET 3

# In[27]:


data3 = pd.read_csv("C:\\Users\\HP\\Downloads\\covid_toy - covid_toy.csv")
data3


# In[28]:


data3.head()


# In[29]:


data3.tail()


# In[30]:


data3.sample(15)


# In[31]:


data3.describe()


# In[32]:


data3.info()


# In[33]:


data3.loc[2:25, ['fever', 'cough']]


# In[34]:


data3.iloc[2:14, 1:3]


# In[35]:


data3['cough'][0] = None
data3


# In[36]:


data3['city'][4] = None
data3


# In[37]:


data3.isnull()


# In[38]:


data3.dropna()


# In[ ]:





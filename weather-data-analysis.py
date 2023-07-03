#!/usr/bin/env python
# coding: utf-8

# # Import Pandas Library

# In[8]:


import pandas as pd


# # Read CSV File

# In[9]:


# r will remove unicode error
data = pd.read_csv(r'/Users/kavitapaliwal/Downloads/dataset/Weather Data Analysis/Weather Data.csv')


# In[7]:


data


# # .head

# In[10]:


data.head() # by default head show only first 5 records


# # .shape

# In[11]:


data.shape # shape shows total rows * columns of the data


# # .index

# In[12]:


data.index  # index shows first and last index of the data


# # .columns

# In[13]:


# shows all the columns name
data.columns  


# # .dtypes

# In[14]:


# its shows the data-type of each columns
data.dtypes


# # .unique()
# 
# in a column, it shows all the uniquevalues.It can be applied on a single column only,not on the whole dataframe

# In[15]:


data['Weather'].unique()


# # .nunique()
# 
# It shows the total no.(count) of unique values in each column. It can be applied on a single column as well as on whole dataframe.

# In[16]:


data.nunique()
#data['Temp_C'].nunique()


# # .count()
# 
# It shows the total no. of non-null values in each column.It can be applied on a single column as well as on whole dataframe

# In[17]:


data.count()


# # .value_counts
# 
# In a column, It shows all the unique values with their count.It can be applied ob single column only. 

# In[18]:


data['Weather'].value_counts()


# # .info()
# 
# Provide basic information about the dataframe

# In[19]:


data.info()


# # Q1: Find all the unique "Wind Speed" values in the data.

# In[20]:


data.columns


# In[21]:


data['Wind Speed_km/h'].nunique()


# In[22]:


data['Wind Speed_km/h'].unique() # 34 unique value


# 
# # Q2: Find the number of times when the "Wheather is exactly Clear"

# In[23]:


data.Weather.value_counts()


# In[42]:


#filtering
data[data['Weather'] == 'Clear']


# In[24]:


# groupby
data.groupby('Weather').get_group('Clear')


# # Q3: Find the number of times when the "Wind Speed was exactly 4km/h"

# In[25]:


data.columns


# In[26]:


data[data['Wind Speed_km/h'] == 4]


# # Q4: Find out all the Null Values in the data.

# In[27]:


data.isnull().sum() # no null value present


# In[28]:


data.notnull().sum()


# # Rename the column name "Weather" of the dataframe to "Weather Condition"

# In[29]:


data.rename(columns = {'Weather' : 'Weather Condition'},inplace=True)#inplace save changes permanetly


# In[30]:


data.head(2)


# # Q6: What is the mean 'Visibility' ?

# In[31]:


data.Visibility_km.mean()


# # Q7: What is the Standard Deviation SD of 'Pressure' ?

# In[32]:


data.Press_kPa.std()


# # Q8: What is the variance of 'relative Humidity' ?

# In[33]:


data['Rel Hum_%'].var() # if any space btw the column name then we use ['']array sign to access data


# # Q9: Find all instances when 'Snow' was recorded 

# In[34]:


# value_counts()
data['Weather Condition'].value_counts()


# In[35]:


#filtering
data[data['Weather Condition'] == 'Snow']


# In[36]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')]


# # Q10: Find all instances when "Wind speed is above 24" and "Visibility is 25"

# In[37]:


data.columns


# In[38]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# # Q11: What is the mean value of each column against each 'Weather Condition'?

# In[47]:


#data.groupby('Weather Condition').mean()



# # Q12: What is the min and max value of each column against each 'Weather Condition'?

# In[80]:


data.groupby('Weather Condition').min()


# In[81]:


data.groupby('Weather Condition').max()


# # Q13: Show all the Records where Weather Condition is Fog.

# In[85]:


data[data['Weather Condition'] == 'Fog']


# # Q14: Find all instances when "Weather is Clear" Or "Visibility is above 40"

# In[92]:


data[(data['Weather Condition'] == 'Clear' ) | (data['Visibility_km'] > 40 )]


# # Q15: Find all instances when:
#         
#     i) "Wheather is Clear" and "Relative humidity is greater then 50"
#     
#     or
#     
#     ii) "visibility is above 40"

# In[93]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km']>40)]


# In[ ]:





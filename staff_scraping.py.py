#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
# Get webpage with requests
web_page = requests.get('https://www.newvisions.org/ams2/pages/our-staff2')


# In[2]:


soup = BeautifulSoup(web_page.text, 'html.parser')


# In[3]:


results = soup.find_all('div', attrs={'class':'matrix-content'})


# In[4]:


print(results)


# In[5]:


# Teacher Name tag: The name is between the tags marked <h5>.
#Position(s) tag: The position(s) is located between the <p>tags after the class tag <div class=”matrix-copy”> .
#The email is between the tags <p> and <em>. Since the<em> tag directly encases the email, that is the tag we will indicate in our scraping code.
test_result = results[0]


# In[6]:


print(test_result)


# In[7]:


test_result.find('h5')
test_result.find('h5').text
test_result.find('p').text.strip('\n\t')


# In[8]:


test_result.find('em').get_text()


# In[10]:


print(st)


# In[11]:


test_result.find('h5')


# In[12]:


df = pd.DataFrame()


# In[13]:


df['Teacher_Names'] = [result.find('h5').text for result in results]


# In[14]:


print(df['Teacher_Names'])


# In[15]:


df['Positions'] = [result.find('p').text.strip('\n\t') for result in results]


# In[16]:


def get_email(teacher_result):
    
    try: 
        email = teacher_result.find('em').get_text()
    except:
        email = teacher_result.find_all('p')[1].text.strip('\n\t')
        
    return email

# Get all emails
df['Email'] = [get_email(result) for result in results]
print(df['Email'])


# In[17]:


print(df.duplicated(['Teacher_Names']).sum())


# In[18]:


df.drop_duplicates(['Teacher_Names'], keep='first', inplace=True)


# In[19]:


df.to_csv('staffdatabase_scraping_practise.csv', index=False)


# In[ ]:





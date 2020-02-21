#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import unidecode
import re
import os
import re
import sys
import unicodedata
import itertools
import pandas as pd
import numpy as np
from collections import Counter
import collections


# In[2]:


songaudio=pd.read_csv("/Users/ospite/Desktop/progetto_mongo/Artisti - integrazione.csv")


# In[3]:


artisturi=pd.read_csv("/Users/ospite/Desktop/progetto_mongo/Artisti.csv")


# In[4]:


artisturi.head()


# In[5]:


songaudio.head()


# In[8]:


songaudio=songaudio.drop(["Unnamed: 0"],axis=1)


# In[ ]:





# In[29]:


def clean(text):
    text=re.sub(r'\[.*\]', '', text)
    text=re.sub(r'\{.*\}', '', text)
    text=re.sub(r'\n',' ',text)
    text=re.sub(r'\r',' ',text)
    return text


# In[10]:


def lower_and_nopunt(text):
    for a in re.findall("([A-Z]+)", text):
        text = text.replace(a, a.lower())
    text = re.sub(r'[^\w\s]', '', text)
    return text


# In[11]:


def nospace(text):
    text=re.sub(r' ','',text)
    return text


# In[12]:


indexNames = artisturi[artisturi['name'].isna() ].index
artisturi.drop(indexNames , inplace=True)


# In[13]:


artisturi["nomepu"]=artisturi["name"].apply(clean)


# In[14]:


artisturi["nomepu"]=artisturi["nomepu"].apply(lower_and_nopunt)


# In[15]:


artisturi["nomepu"]=artisturi["nomepu"].apply(nospace)


# In[16]:


indexNames = songaudio[songaudio['Artist'].isna() ].index
songaudio.drop(indexNames , inplace=True)


# In[17]:


songaudio["nomepu"]=songaudio["Artist"].apply(clean)


# In[18]:


songaudio["nomepu"]=songaudio["nomepu"].apply(lower_and_nopunt)


# In[19]:


songaudio["nomepu"]=songaudio["nomepu"].apply(nospace)


# In[20]:


dfqf=pd.merge(songaudio, artisturi,left_on="nomepu", right_on="nomepu", how='inner')


indexNames = dfqf[dfqf['Lyrics'].isna() ].index
dfqf.drop(indexNames , inplace=True)


# In[24]:


def contaparoletot(text):
    words = re.findall(r'\w+',text)
    parole=Counter(words)
    return sum(parole.values())


# In[25]:


def contaparolemin(text):
    words = re.findall(r'\w+',text)
    parole=Counter(words)
    return len(parole)


# In[30]:


dfqf["lyr_pu"]=dfqf["Lyrics"].apply(clean)


# In[27]:


dfqf["lyr_pu"]=dfqf["lyr_pu"].apply(lower_and_nopunt)


# In[33]:


dfqf["paroletot"]=dfqf["lyr_pu"].apply(contaparoletot)


# In[34]:


dfqf["parolemin"]=dfqf["lyr_pu"].apply(contaparolemin)


# In[37]:


dfqf["indice"]=(1-(dfqf["parolemin"]/dfqf["paroletot"]))


# In[ ]:





# In[ ]:





# In[40]:


ale=pd.read_csv("/Users/ospite/Desktop/progetto_mongo/AudioFeatureIntegrazioneAle.csv")


# In[41]:


indexNames = ale[ale['Lyrics'].isna() ].index
ale.drop(indexNames , inplace=True)



ale=ale.drop(["Unnamed: 0.1"],axis=1)


# In[46]:


ale["lyr_pu"]=ale["Lyrics"].apply(clean)


# In[47]:


ale["lyr_pu"]=ale["lyr_pu"].apply(lower_and_nopunt)


# In[48]:


ale["paroletot"]=ale["lyr_pu"].apply(contaparoletot)


# In[49]:


ale["parolemin"]=ale["lyr_pu"].apply(contaparolemin)


# In[50]:


ale["indice"]=(1-(ale["parolemin"]/ale["paroletot"]))


# In[82]:



# In[94]:


a = [dfqf, ale]
dfinal = pd.concat(a)
len(dfinal)


# In[95]:


dfinal.drop_duplicates(subset=['Artist', 'Title'], keep='first',inplace=True)



dfinal.to_csv("dfinal.csv")


# In[ ]:





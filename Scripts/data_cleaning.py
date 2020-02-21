#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re
from datetime import datetime


# In[ ]:


dfinal = pd.read_csv("C:/Users/Angela/Desktop/rounded_perviz_2.csv", sep = ",")


# In[ ]:


def trasforma(data):
    try:
        data = datetime.strptime(data, "%Y-%m-%d")
        data = int(data.year)
        return (data)
    except:
        return(data)   
def trasforma_mese(data):
    try:
        data = datetime.strptime(data, "%Y-%m")
        data = int(data.year)
        return (data)
    except:
        return(data)       
    


# In[ ]:


dfinal["Date"] = dfinal["RELEASE_DATE"].apply(trasforma)
dfinal["Date"] = dfinal["Date"].apply(trasforma_mese)
dfinal["Date"] = dfinal["Date"].fillna("")


# In[ ]:


df["Date"] = df["Release_Date_T"].apply(trasforma)
df["Date"] = df["Date"].apply(trasforma_mese)
df["Date"] = df["Date"].fillna("")
df.groupby("Date").count()


# In[ ]:


dfinal.to_csv("date_pulite.csv")


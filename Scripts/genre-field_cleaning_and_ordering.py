#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


df = pd.read_csv("complete_noperviz.csv", sep =",")


# In[3]:


dfgruppato=[df.groupby("Artist_A").mean()["indice"]]


# In[4]:


dfgruppato=pd.DataFrame(dfgruppato)


# In[5]:


dfgruppato = dfgruppato.transpose()


# In[6]:


dfgruppato = dfgruppato.reset_index()


# In[7]:


dfgruppato.head()


# In[8]:


def clean(text):
    text=re.sub(r'\[','',text)
    text=re.sub(r'\]','',text)

    return text


# In[9]:


def cleanv(text):
    text=re.sub(r'\'','',text)

    return text


# In[10]:


df["generi_tot"]=df["generi_tot"].fillna("")


# In[11]:


df["generi_tot"]=df["generi_tot"].apply(clean)
df["generi_tot"]=df["generi_tot"].apply(cleanv)


# In[12]:


df["generi_tot"]


# In[13]:


df["generisplit"]=[x.split(",") for x in df["generi_tot"]]
df["lengen"]=df["generisplit"].apply(len)
df.head()
                   


# In[19]:


df["generi_tot"].unique()


# In[ ]:


len(df)


# In[ ]:


df[df["lengen"]==11]


# In[20]:


dftrans=df["generisplit"].apply(pd.Series)
dftrans


# In[21]:


nomi=pd.DataFrame(df["Artist_A"])


# In[ ]:


nomi.head()


# In[24]:


definitivo=pd.merge(dftrans,nomi,left_index=True,right_index=True)                   .melt(id_vars=["Artist_A"],value_name="genereunico")                   .drop("variable",axis=1)                   .dropna()
definitivo


# In[26]:


definitivo[definitivo["genereunico"] == "rap,trap"]


# In[ ]:


def clean_spazi(text):
    text=re.sub(r' ','',text)
    text=re.sub(r' ','',text)
    return text


# In[ ]:


definitivo["genereunico"] = definitivo["genereunico"].apply(clean_spazi)


# In[ ]:


definitivo.drop_duplicates(["Artist_A","genereunico"],inplace=True,keep="first")


# In[ ]:


definitivo


# In[ ]:


def clean_doppi(text):
    text=re.sub('hiphophiphop','hiphop',text)
    text=re.sub('countrycountry','country',text)
    text=re.sub('jazzjazz','jazz',text)
    text=re.sub('alternativealternative','alternative',text)
    text=re.sub('discodisco','disco',text)
    text=re.sub('poppop','pop',text)
    text=re.sub('househouse','house',text)
    text=re.sub('traptrap','trap',text)
    text=re.sub('rockrock','rock',text)
    text=re.sub('dancedance','dance',text)
    text=re.sub('electroelectro','electro',text)
    text=re.sub('raprap','hiphop',text)
    text=re.sub('rap','hiphop',text)
    text=re.sub('latinhiphop','latin',text)
    text=re.sub('folkpop','folk',text)
    
    text=re.sub('dancepop','dance',text)
    text=re.sub('electropop','electro',text)
    text=re.sub('hiphoppop','hiphop',text)
    text=re.sub('latinpop','latin',text)
    text=re.sub('housepop','house',text)
    text=re.sub('thiphop','hiphop',text)
    text=re.sub('rockpop','rock',text)
 
    return(text)


# In[ ]:


print(count)


# In[ ]:


definitivo["genereunico"] = definitivo["genereunico"].apply(clean_doppi)


# In[ ]:


a = definitivo.groupby("genereunico").count()
a = a.reset_index()
a =a[a["Artist_A"]<=15]
ilsta_da_droppare = a["genereunico"]


# In[ ]:


ilsta_da_droppare


# In[ ]:


definitivo["genereunico"] =definitivo["genereunico"].fillna("")


# In[ ]:


definitivo = definitivo.reset_index()
definitivo = definitivo.drop("index", 1)


# In[ ]:


ilsta_da_droppare = ilsta_da_droppare.reset_index()
ilsta_da_droppare = ilsta_da_droppare.drop("index", 1)


# In[ ]:


indexNames = list()
for i in range(0,len(definitivo)):
    print (i)
    genere = definitivo["genereunico"][i]
    for h in range(0,len(ilsta_da_droppare)):
        if genere == ilsta_da_droppare["genereunico"][h]:
            print(genere)
            indexNames.append(i)        


# In[ ]:


len(indexNames)


# In[ ]:


definitivo = definitivo.drop(indexNames, 0 )


# In[ ]:


definitivo.groupby("genereunico").count()  


# In[ ]:


definitivo = definitivo.drop_duplicates(["Artist_A", "genereunico"])


# In[ ]:


definitivo.sort_values("Artist_A")


# In[ ]:


pervizgenere=pd.merge(definitivo,dfgruppato,on="Artist_A",how="left")
pervizgenere.sort_values("Artist_A")


# In[ ]:


pervizgenere.to_csv("pervizgenere.csv")


# In[ ]:


pervizgenere.groupby("genereunico").count()


# In[ ]:





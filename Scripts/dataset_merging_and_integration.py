#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import re


# In[2]:


grande = pd.read_csv("C:/Users/Angela/Desktop/finali/dfinal_piugeneri.csv", sep = ",")
piccolo = pd.read_csv("C:/Users/Angela/Desktop/finali/CompletamentoAle.csv", sep = ",")


# In[3]:


grande = grande.drop("Unnamed: 0.1",1)
grande = grande.drop("Unnamed: 0",1)


# In[4]:


grande.columns = ["Markets_T", "Artist_A", "Url_T", "id_T", "Lyrics_T", 
                  "Popularity_T", "Release_Date_T", "Title_T","id_A", 'acousticness',
                  'danceability', 'duration_ms', 'energy', 'follower', 'genres', 'indice',
                  'instrumentalness', 'liveness', "loudness_T","Lyrics_clean_T", "Name2","Artist_clean_A", 
                  "Parole_min_T", "Parole_tot_T", "Popularity_A", "speechiness_T", "Url_A", "valence_T", 
                  "generi_puiti"]


# In[5]:


piccolo


# In[7]:


complete = pd.merge(grande,piccolo, left_on = "Artist_A", right_on = "Artist", how = "left" )


# In[ ]:


for i in range(0,len(complete)):
    print(i)
    if (complete["genres_y"][i] != "[]"):
        complete["generi_puiti"][i] = complete["genres_y"][i]  
    if (complete["follower"][i] != "[]"):
        complete["foll"][i] = complete["genres_y"][i] 
        if (complete["genres_y"][i] != "[]"):
        complete["generi_puiti"][i] = complete["genres_y"][i] 
        if (complete["genres_y"][i] != "[]"):
            complete["generi_puiti"][i] = complete["genres_y"][i]     


# In[31]:


def clean(gen):
    gen = re.sub(r'\[]', "",gen)
    return (gen)


# In[36]:


complete["genres_y"]


# In[54]:


complete


# In[53]:


complete["sp_artist_url"] = complete["sp_artist_url"].fillna("")
complete["Url_A"] = complete["Url_A"].fillna("")
complete["Url_A_tot"] = complete["Url_A"] + complete["sp_artist_url"]


# In[62]:


#complete = complete.drop("follower", 1)
complete = complete.drop("genres_x", 1)


# In[64]:


#complete.to_csv("complete_noperviz.csv")


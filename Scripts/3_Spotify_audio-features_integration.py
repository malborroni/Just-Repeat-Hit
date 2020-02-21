#!/usr/bin/env python
# coding: utf-8

# In[2]:

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint
import pandas as pd
cid ="a1a6ca81330845b1b9bafa42d34c4eff" 
secret = "d4cd89e3ca1b458e92837c9fab5f5dac"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[3]:

df = pd.read_csv("Lyrics.csv", sep = ",")
df["ID_TRACK"] = ""
df["POPULARITY"] = ""
df["RELEASE_DATE"] = ""
df["EXTERNAL_URLS"] = ""
df["AVAILABLE_MARKETS"] = ""
df["danceability"] = ""
df["energy"] = ""
df["loudness"] = ""
df["speechiness"] = ""
df["acousticness"] = ""
df["instrumentalness"] = ""
df["liveness"] = ""
df["valence"] = ""
df["duration_ms"] = ""


# In[4]:


def find_track_ID(artist, track,i):
    try:
        track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')    
        #pprint.pprint(track_id)
        ID_TRACK = track_id['tracks']['items'][0]['id']
        #print(ID_TRACK)
        POPULARITY = track_id['tracks']['items'][0]['popularity']
        #print(POPULARITY)
        RELEASE_DATE = track_id['tracks']['items'][0]['album']['release_date']
        EXTERNAL_URLS = track_id['tracks']['items'][0]['album']['external_urls']['spotify']
        AVAILABLE_MARKETS = len(track_id['tracks']['items'][0]['album']['available_markets'])

        df["ID_TRACK"][i] = ID_TRACK
        df["POPULARITY"][i] = POPULARITY
        df["RELEASE_DATE"][i] = RELEASE_DATE
        df["EXTERNAL_URLS"][i] = EXTERNAL_URLS
        df["AVAILABLE_MARKETS"][i] = AVAILABLE_MARKETS
        #audio_features
        af = sp.audio_features(str(ID_TRACK))[0]
        df["danceability"][i]= af["danceability"]
        df["energy"][i] = af["energy"]
        df["loudness"][i] = af["loudness"]
        df["speechiness"][i] = af["speechiness"]
        df["acousticness"][i] = af["acousticness"]
        df["instrumentalness"][i] = af["instrumentalness"]
        df["liveness"][i] = af["liveness"]
        df["valence"][i] = af["valence"]
        df["duration_ms"][i] = af["duration_ms"] 
    except:
        print("Errore")
        df["ID_TRACK"][i] = None
        df["POPULARITY"][i] = None
        df["RELEASE_DATE"][i] = None
        df["EXTERNAL_URLS"][i] = None
        df["AVAILABLE_MARKETS"][i] = None
        df["danceability"][i]= None
        df["energy"][i] = None
        df["loudness"][i] = None
        df["speechiness"][i] = None
        df["acousticness"][i] = None
        df["instrumentalness"][i] = None
        df["liveness"][i] = None
        df["valence"][i] = None
        df["duration_ms"][i] = None


# In[ ]:


for i in range(0,len(df)):
    print(i)
    find_track_ID(df["Artist"].iloc[i],df["Title"].iloc[i], i)
print("############## ho finito ############")


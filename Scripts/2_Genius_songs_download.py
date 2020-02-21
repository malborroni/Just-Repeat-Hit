#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import lyricsgenius as genius

geniusCreds = "1JWlkyRPDtsPsd4ooQam5qrNzyKe7kh-G9-DMZ59BsVMaK23JoI6zAphdWQvSDiE"

df = pd.read_csv('Artisti.csv', sep = ',')

a =df["name"]
a = list(a)
artist = list()
title = list()
lyrics = list()
conta = 0
n_song = 10
for count, c in enumerate (a):
    if (count % 1000 == 0):
        try:
            api = genius.Genius(geniusCreds)
        except Exception as e:
            print("error in client", e)
            time.sleep(10)
            api = genius.Genius(geniusCreds)
    try: 
        res = api.search_artist(c, max_songs = n_song)
    except Exception as e:
        print("Error in client", e)
        api = genius.Genius(geniusCreds)
    if(res != None):
        for i in range(0,len(res.songs)):
            if (len(res.songs) != 0):
                artist.append(res.songs[i].artist)
                title.append(res.songs[i].title)
                lyrics.append(res.songs[i].lyrics)
            else:
                artist.append(c)
                title.append("?")
                lyrics.append("?") 
    else:
        artist.append(c)
        title.append("?")
        lyrics.append("?")  
             
            
canzoni = pd.DataFrame({"Artist" : artist, "Title": title, "Lyrics": lyrics})

canzoni.to_csv("Lyrics.csv", sep = ',')


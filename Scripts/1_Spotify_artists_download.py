#!/usr/bin/env python
# coding: utf-8

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd
import pymongo
from pymongo import MongoClient

cid ="f2edcce358934598a27da7bf4ba92082" 
secret = "5c7c7158908a48f79ad2bba8faa6f2c2"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


client=MongoClient('localhost',27017)

db=client.Progetto
singer=db.singer

alphabet = ["a*, b*, c*, d*, e*, f*, g*, h*, i*, j*, k*, l*, m*, n*, o*, p*, q*, r*, s*, t*, u*, v*, w*, x*, y*, z*"]

conta = 0
import pprint
for x in alphabet:
    print("Lettera: " + x )
    artist_res = sp.search(q=x ,type = 'artist')
    for i in range(0, artist_res["artists"]["total"] // 50):
        artist_res = sp.search(q=x ,type = 'artist', limit = 50,offset=i)
        for i, t in enumerate(artist_res['artists']['items']):
            conta = conta + 1
            id = conta
            #print(id)
            name = t['name'].encode(encoding = 'UTF-8',errors = 'replace')
            #print(name)
            url = (t['external_urls']['spotify']).encode(encoding = 'UTF-8',errors = 'replace')
            #print(url)
            follower = t['followers']['total']
            #print(follower)
            genres = (t['genres'])
            #print(genres)
            popularity = t['popularity']
            #print(popularity)
            n_art = {'id_': id, 'name': name,'follower': follower, 'genres':genres, 'popularity': popularity, 'url':url}
            singer.insert_one(n_art)
print('Script terminato')



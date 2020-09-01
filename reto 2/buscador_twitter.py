# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 06:49:18 2019

@author: jairo
"""
"import twitter" 
import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt




"""
Funcion para que verificarse ante la api
"""
def entrar():
    auth = tw.OAuthHandler("YAve8QoP6jEbswUj3wL1jnZqF", "OxXPta9Wx67GnOnmSmyR8dHAriXOfcEvpHlUpmXvqCq8YbyRZR")
    auth.set_access_token("1138192133029072897-waIckoLbFnM4ZeOwkAOKSrjmMTji5N", "Vxlqf17CmexhIC1nPBXsoOYteV4xSZXQwTHz0GVqJrTor")
    ap = tw.API(auth)
    consultar(ap)
    
"""
funcion para realizar las consultas
"""
def consultar(ap):
    df=pd.read_csv("registro1.csv")
    """
    Latitudes y longitudes tomadas de diferentes pueblos
    """
    coor=[['4.6097100','-74.0817500'],['4.717','-73.967'],['4.817','-74.367'],['4.73245','74.2641907'],['4.8136700','-74.3545300'],['4.52748','-73.9257'],['4.8587599','-74.0586624'],['5.30667','-73.8144']]
    
    llaves=['Zona A','Zona B','Zona C','Zona D','Zona E','Zona F','Zona G','Zona H']
    
    #data=[[0]*8,[0]*8,[0]*8,[0]*8]
    #df = pd.DataFrame(data)
    
    for x in coor:
    
        lugar=ap.geo_search(lat=x[0],long=x[1],max_results=1)
        for tweet in tw.Cursor(ap.search,q='place:'+lugar[0].id).items(2):
            print(tweet.source)
                
            if tweet.source=='Twitter for iPhone' or tweet.source=='Twitter Web App':
                    df.iloc[coor.index([x[0],x[1]]),1]=int(df.iloc[coor.index([x[0],x[1]]),1])+1
                
            else:   
                     df.iloc[coor.index([x[0],x[1]]),2]=int(df.iloc[coor.index([x[0],x[1]]),2])+1
           
    a=df[1].sum()
    b=df[2].sum()
    if a!=0:
        df[3]/=a
        
    if b!=0:
        df[4]/=b
    df.to_csv("registro1.csv")    

entrar()
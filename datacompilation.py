# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:55:45 2020

@author: Aquib Akhtar
"""

import sqlite3
from pytrends.request import TrendReq
import pandas as pd




    
conn=sqlite3.connect('database.db')
c=conn.cursor()

#c.execute('''DROP TABLE highscore''')
c.execute('''
              
              CREATE TABLE IF NOT EXISTS userData
              (userpass STRING, 
              useremail STRING,
              userdisplayname STRING,
              score INTEGER)
              ''')
    
c.execute('''
              CREATE TABLE IF NOT EXISTS highscore
              (userDisplay INTEGER,
              highscore INTEGER,
              FOREIGN KEY(userDisplay) REFERENCES userData(userdisplayname))
              ''')
              
c.execute('''          
              CREATE TABLE IF NOT EXISTS searchKey
              (searchTerm STRING UNIQUE)
              ''')
              
c.execute('''         
              CREATE TABLE IF NOT EXISTS categories
              (cat STRING)
              ''')
             
c.execute('''
              CREATE TABLE IF NOT EXISTS searchTerms
              (searchTerm STRING,
              cat STRING,
              r1 STRING,
              r2 STRING,
              r3 STRING,
              r4 STRING,
              FOREIGN KEY(searchTerm) REFERENCES searchKey(searchTerm),
              FOREIGN KEY(cat) REFERENCES categories(cat))
              ''')
              
              
conn.commit()
conn.close()

"""
conn=sqlite3.connect('database.db',isolation_level=None)
c= conn.cursor()
c.execute('''
              INSERT INTO categories VALUES
              ('Pop');''')

c.execute('''
              INSERT INTO categories VALUES
              ('Food and Drink');''')
c.execute('''
              INSERT INTO categories VALUES
              ('Sport');''')

c.execute('''
              INSERT INTO categories VALUES
              ('Books & Literature');''')

c.execute('''
              INSERT INTO categories VALUES
              ('Games');''')
c.close()
"""


pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=2, backoff_factor=0.1)



def GetDataFrame(searchTerm):
    
    pytrends.build_payload(kw_list=[searchTerm])
    df = pytrends.interest_by_region()
    df=df.nlargest(4,[searchTerm])
    addSearchTerm(searchTerm,df)

def addSearchTerm(searchTerm,df):
    df=df.index
    
    #Add Search Term
    
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              INSERT INTO searchKey VALUES
              (?);''')
    c.execute(param,[str(searchTerm)],)
    conn.close()
    
    #add to searchTermsDB
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              INSERT INTO searchTerms VALUES
              (?,?,?,?,?,?);''')
    
    paramarray=[searchTerm,'Games',df[0],df[1],df[2],df[3]]
    c.execute(param,paramarray,)
    conn.close()
    

userTerm="temp"
while userTerm != "":
    userTerm=input("Enter Your Search Term  ")
    GetDataFrame(userTerm)
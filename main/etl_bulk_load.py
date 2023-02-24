#!/usr/bin/env python
# coding: utf-8

# Import library 
import pandas as pd
import os
import time
import schedule

#Give the file path 
cwd = os.path.abspath(r"C:\Users\Documents\bulk_load") 
files = os.listdir(cwd)
df = pd.DataFrame()

#Append for the new data 
for file in files:
     if file.endswith('.xlsx'): 
        df = df.append(pd.read_excel(file),ignore_index = True) #read and append if it is new .xlsx file


#Connect to postgres Engine
from sqlalchemy import create_engine
from datetime import datetime


#credential
conn_string = 'postgresql+psycopg2://username:password@host:port/database'
db = create_engine(conn_string)
conn = db.connect()

#Push to postgres and set query duration
start_time = time.time()
df.to_sql(
    'sale_transaction', 
    con = conn,
    if_exists = "append",
    schema='public',   
    index=False,
)
print("to_sql duration: {} seconds".format(time.time() - start_time))



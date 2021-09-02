#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

#here we read csv files then there two coulumns orderdate and sales  on a particular date.

df= pd.read_csv("Orders_WithNulls2.csv", usecols = ['Orderdate' , 'Sales'])

print(df)


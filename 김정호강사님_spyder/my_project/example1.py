# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:00:55 2019

@author: student
"""
from datetime import datetime as dt
current = dt.now()
print("{:%Y-%m-%d %H:%M:%S}".format(current))
print(current.year)
print(current.month)
print(current.day)
print(current.hour)
print(current.minute)
print(current.second)


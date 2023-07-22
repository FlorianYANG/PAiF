#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
sns.set()

path = r"D:\Programming\Python\utils\playg"
file = os.path.join(path, "USyield.xlsx")
data = pd.read_excel(file,index_col=0)

# data = data.fillna(method="ffill")
# data.plot(figsize=(10,6))

col = data.columns
index = data.index
data[col[0]].plot(figsize= (14,8))

select = range(10,700,20)
l = len(col)
gap = 4

for i in select:
    sliceY = data.iloc[i].T
    sliceD = index[i:i+l*gap:gap]
    sliceY.index = sliceD
    sliceY.plot(alpha = 0.8, style=".")


#!/usr/bin/python3.8

import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib as plt

cats = pd.read_csv("./cats_joined.csv")
cats['date_column'] = cats['timestamp'].str[:10]
# cats['date_column'] = pd.to_datetime(cats['timestamp'])
cats['ymd'] = cats['date_column'].dt.date

print(cats.shape)
# print(cats.describe())
print(cats.dtypes)

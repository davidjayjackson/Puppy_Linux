import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib as plt

cats = pd.read_csv("./cats_uk.csv")
cats['date_column'] = cats['timestamp'].str[:10]
# cats['date_column'] = pd.to_datetime(cats['timestamp'])

cats['ymd'] = cats['date_column'].dt.date
print(cats.shape)


# remove spaces and convert to lowercase
cats['tag_id'] = cats['tag_id'].str.strip().str.lower()

print(cats.shape)

cats_references = pd.read_csv("./cats_uk_reference.csv")
print(cats_references.shape)
 
# remove spaces and convert to lowercase
cats_references['tag_id'] = cats_references['tag_id'].str.strip().str.lower()
print(cats.shape)

cats_joined = pd.merge(cats_references['tag_id'], cats, on="tag_id")
cats_joined.to_csv("./cats_joined.csv", index=False)

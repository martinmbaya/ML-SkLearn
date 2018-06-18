import pandas as pd
import numpy as np

name = "mushrooms.csv"

df = pd.read_csv(name,header='infer', na_values="?" )
print(df.head())
print(df.dtypes)

#Replace the label values with one or zero
cleanup_nums = {"class":     {"e": 1, "p": 0} }
df.replace(cleanup_nums, inplace=True)

#One Hot Encoding
df=pd.get_dummies(df, columns=None)

print(df.dtypes)
df.to_csv("mushroom_edit.csv", sep=',', encoding='utf-8')

print(df[df.isnull().any(axis=1)])
import os
import pandas as pd
os.chdir(r"C:\Users\niki\Downloads\datasets\housing")
df = pd.read_csv("housing.csv")
x =  df.groupby('ocean_proximity').count()[['longitude']]
print(x)
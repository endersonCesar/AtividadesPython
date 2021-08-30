import numpy as np
import pandas as pd


df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

data_query = df.loc[(df.weekday ==6)  &  (df.hour ==13),'total_count'].mean()
print(data_query)

# 13 - 385.37142857142857
# 17 - 334.4095238095238
# 7 - 45.96190476190476
# 21 -156.0
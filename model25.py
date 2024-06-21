"""Write a python program will take in a dataset containing daily temperature readings for each city over a year and perform the following tasks:
·       Calculate the mean temperature for each city.
·       Calculate the standard deviation of temperature for each city.
·       Determine the city with the highest temperature range (difference between the highest and lowest temperatures).
·       Find the city with the most consistent temperature (the lowest standard deviation).
"""
import pandas as pd
import numpy as np
np.random.seed(0)
days=pd.date_range(start='2023-01-01',periods=365)
city_data={
     'CityA': np.random.normal(loc=15, scale=10, size=365),
     'CityB': np.random.normal(loc=20, scale=5, size=365),   
    'CityC': np.random.normal(loc=25, scale=8, size=365)
     }
df=pd.DataFrame(city_data)
print("datset preview:\n",df)
mean_temp=df.mean()
print("mean temperature for each city:",mean_temp)
std=df.std()
print("standard deviation of temperature for each city:",std)
temp_ranges=df.max()-df.min()
city_with_highest_range=temp_ranges.idxmax()
highest_range=temp_ranges.max()
print(f"city with highest temperature range:{city_with_highest_range} ({highest_range}celsius)")
city_with_lowest_std_dev=std.idxmin()
lowest_std=std.min()
print(f"city with the most consistent temperature:{city_with_lowest_std_dev} (standard deviation:{lowest_std} celsius)")

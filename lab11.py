"""You are a data scientist working for a medical research institute. The institute is conducting a study to understand the relationship between smoking habits and the incidence of lung cancer among a group of individuals. As part of your analysis, you are tasked with calculating the correlation coefficient between smoking and lung cancer rates and creating a scatter plot to visualize the data.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
data={
    'SmokingRate': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    'LungCancerRate': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
df=pd.DataFrame(data)
print("dataset preview:\n",df.head())
correlation_coefficient,_=pearsonr(df['SmokingRate'],df['LungCancerRate'])
print("\ncorrelation coefficient between smoking reate and lung cancer rate:",correlation_coefficient)
#scatterplot
plt.figure(figsize=(10,5))
sns.scatterplot(x='SmokingRate',y='LungCancerRate',data=df)
plt.title("scatter plot for smoking rates vs  lung cancer rate")
plt.xlabel("smoking Rate")
plt.ylabel("lung cancer rate")
plt.grid(True)
plt.show()


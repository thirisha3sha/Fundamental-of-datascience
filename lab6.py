"""Scenario : You are a data scientist working for a company that sells products online. You have been tasked with creating a simple plot to show the sales of a product over time.
Question:
1. Write code to create a simple line plot in Python using Matplotlib to predict sales happened in a month?
2. Write code to create a scatter plot in Python using Matplotlib to predict sales happened in a month?
3. Develop a Python program to create a bar plot of the monthly sales data."""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats
days=np.arange(1,31)
sales=np.random.randint(100,500,size=30)
data={
    'Day':days,
    'Sales':sales
    }
df=pd.DataFrame(data)
print("sales data over a month:\n",df)
#lineplot
plt.figure(figsize=(10,5))
plt.plot(df['Day'],df['Sales'],marker='o',linestyle='-',color='b')
plt.title('sales over a month')
plt.xlabel('Day')
plt.ylabel('sales')
plt.show()
#scatterplot
plt.figure(figsize=(10,5))
plt.scatter(df['Day'],df['Sales'])
plt.xlabel('Day')
plt.ylabel('Sales')
plt.title("scatter plot in sales over a month")
plt.grid(True)
plt.show()
#barplot
plt.figure(figsize=(10,5))
plt.bar(df['Day'],df['Sales'],color='g')
plt.title("Sales over a month")
plt.xlabel('Day')
plt.ylabel('Sales')
plt.grid(True,axis='y')
plt.show()
#histogram
plt.figure(figsize=(10,5))
sns.histplot(df['Sales'],bins=10,kde=True,color='b')
plt.title('Sales distribution over a month(Histogram)')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
#qq plot
plt.figure(figsize=(10,5))
stats.probplot(df['Sales'],dist='norm',plot=plt)
plt.title("Q-Q plot of sales data")
plt.xlabel("Theoritical quantiles")
plt.ylabel("sample quantiles")
plt.grid(True)
plt.show()

          

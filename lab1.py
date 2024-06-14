"""Suppose a hospital tested the age and body fat data for 18 randomly selected adults
with the following result.
Question: 
Calculate the mean, median and standard deviation of age and %fat using Pandas.
Draw the boxplots for age and %fat.
Draw a scatter plot and a q-q plot based on these two variables"""
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
data={
    'age':[23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'fat_percent':[9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
    }
df=pd.DataFrame(data)
print("dataset:\n",df)
mean_age=df['age'].mean()
median_age=df['age'].median()
mode_age=df['age'].mode()[0]
std_age=df['age'].std()
mean_fat_percent=df['fat_percent'].mean()
median_fat_percent=df['fat_percent'].median()
mode_fat_percent=df['fat_percent'].mode()[0]
std_fat_percent=df['fat_percent'].std()
print("AGE:")
print("mean:",mean_age)
print("median:",median_age)
print("mode:",mode_age)
print("standard deviation:",std_age)
print("FAT PERCENT:")
print("mean:",mean_fat_percent)
print("median:",median_fat_percent)
print("mode:",mode_fat_percent)
print("standard deviation:",std_fat_percent)
#boxplot
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
df['age'].plot(kind='box')
plt.title("boxplot for age")
plt.subplot(1,2,2)
df['fat_percent'].plot(kind='box')
plt.title("boxplot of fat percent")
plt.show()
#scatterplot
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.scatter(df['age'],df['fat_percent'])
plt.xlabel("age")
plt.ylabel("fat_percent")
plt.title("scatter plot")
plt.subplot(1,2,2)
stats.probplot(df['age'],dist="norm",plot=plt)
plt.title("Q-Q plot for age")
plt.show()
               
    

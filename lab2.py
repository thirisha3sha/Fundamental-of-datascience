"""You are working with an e-commerce company that has collected data on the purchase amounts made by customers over the past month.
The dataset includes the purchase amounts (in dollars) for each transaction.
Utilize measures of central tendency to answer the following questions:
Calculate the mean (average) purchase amount to understand the typical spending behavior of customers.
Identify the mode of the purchase amounts to find the most frequently occurring purchase amount, helping the company understand popular spending levels"""
from scipy import stats
import pandas as pd
data={
    'Transaction_id':[1,2,3,4,6,23,45,6,7,99,56],
    'purchase_amounts':[20, 30, 40, 40, 50, 50, 50, 60, 70, 80, 90]
    }
df=pd.DataFrame(data)
print("\npurchasing dataset of e-commerce company:\n",df)
mean=sum(df['purchase_amounts'])/ len(df['purchase_amounts'])
mode=df['purchase_amounts'].mode()[0]
print("mean for purchase amounts:",mean)
print("mode for purchase amounts:",mode)

"""Scenario: You are a data analyst working for a company that sells products online. You have been tasked with analyzing the sales data for the past month. The data is stored in a Pandas data frame.
Question: Develop a code in python to find the frequency distribution of the ages of the customers who have made a purchase in the past month."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data={
    'cutomer_id':list(range(1,11)),
    'customer_age':[22,23,22,24,55,44,44,44,55,67],
    'purchase_amount':[100,200,100,400,500,200,688,344,566,4555],
    'purchase_date':pd.date_range(start='2024-05-01',periods=10,freq='D')
    
    }
sales_data=pd.DataFrame(data)
age_distribution=sales_data['customer_age'].value_counts().sort_index()
print("Frequency of age distribution:",age_distribution)
#barplot
plt.figure(figsize=(10,5))
sns.barplot(x=age_distribution,y=age_distribution.values,palette='viridis')
plt.title("frequency didtribution of customer age")
plt.xlabel("Customer age")
plt.ylabel("Frequency")
plt.show()


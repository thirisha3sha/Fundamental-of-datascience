"""you are a data analyst working for an e-commerce company. The company has provided you with a dataset containing information about customer orders. The dataset includes columns such as OrderID, CustomerID, ProductID, Quantity, and TotalPrice. Your task is to use Panda’s data frames to analyze and derive insights from the dataset.
"""
import pandas as pd
data={
    'order_id':list(range(1,11)),
    'customer_id':list(range(101,111)),
    'product_id':[11,12,23,23,12,23,56,78,12,23],
    'quantity':[1,2,1,3,2,4,2,3,1,1],
    'total_price':[20.0, 40.0, 15.0, 60.0, 40.0, 60.0, 40.0, 60.0, 20.0, 20.0]
    }
df=pd.DataFrame(data)
print("Dataset preview:\n",df.head())
print("\nDataframe Information:\n",df.describe())
total_sales=df['total_price'].sum()
print("\ntotal sales:\n",total_sales)
quantity_per_product=df.groupby('product_id')['quantity'].sum()
print("\nTotal quantity sold per product:\n",quantity_per_product)
avg_order_value=df['total_price'].mean()
print("\nAverage order value:\n",avg_order_value)
orders_per_customer=df['customer_id'].value_counts()
print("\nNumber of orders per customers:\n",orders_per_customer)
# Identifying top customers by total spending
top_customers=df.groupby('customer_id')['total_price'].sum().sort_values(ascending=False)
print("\n top Customers by total spending:\n",top_customers)





                    

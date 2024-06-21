"""You are working as a data analyst for an e-commerce company. You have been
given a dataset containing information about customer orders, stored in a Pandas DataFrame
named order_data. The DataFrame has columns for customer ID, order date, product name,
and order quantity. Your task is to analyze the data and answer specific questions about the
orders.
Question: Using Pandas DataFrame operations, how would you find the following
information from the order_data DataFrame:
1. The total number of orders made by each customer.
2. The average order quantity for each product.
3. The earliest and latest order dates in the dataset."""
import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 1, 3, 2, 1, 4, 3, 4, 2],
    'order_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', 
                   '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'],
    'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B',
                     'Product A', 'Product C', 'Product B', 'Product C', 'Product A'],
    'order_quantity': [2, 1, 3, 5, 2, 1, 4, 2, 1, 3]
}

# Create DataFrame
order_data = pd.DataFrame(data)

# Convert 'order_date' to datetime format
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# Total number of orders made by each customer
total_orders_by_customer = order_data.groupby('customer_id').size().reset_index(name='total_orders')
print("Total number of orders made by each customer:")
print(total_orders_by_customer)

# Average order quantity for each product
average_order_quantity_by_product = order_data.groupby('product_name')['order_quantity'].mean().reset_index()
print("\nAverage order quantity for each product:")
print(average_order_quantity_by_product)

# Earliest and latest order dates
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)

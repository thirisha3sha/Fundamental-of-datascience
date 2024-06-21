""" Scenario: You are a manager at a retail store and need to calculate the total revenue from a recent promotion, including discounts and taxes. You have the sales prices and quantities sold for each item, and the discount and tax rates are provided as percentages. Your task is to compute the total revenue generated after applying discounts and taxes.
Question: Use arithmetic operations to calculate the total revenue from the promotion, including discounts and taxes, given the sales prices, quantities sold, discount rate, and tax rate?
"""
import pandas as pd

# Sample data (mock data)
data = {
    'Item': ['Product A', 'Product B', 'Product C'],
    'Sales_Price': [50, 80, 30],  # Sales prices in dollars
    'Quantity_Sold': [100, 50, 80],  # Quantities sold
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame (optional)
print(df)

# Constants for discount rate (%) and tax rate (%)
discount_rate = 10  # 10% discount
tax_rate = 7  # 7% tax

# Calculate total revenue before any discounts or taxes
df['Total_Sales'] = df['Sales_Price'] * df['Quantity_Sold']

# Apply discount
df['Discounted_Amount'] = df['Total_Sales'] * (1 - discount_rate / 100)

# Apply tax on discounted amount
df['Total_Revenue'] = df['Discounted_Amount'] * (1 + tax_rate / 100)

# Calculate total revenue from the promotion
total_revenue = df['Total_Revenue'].sum()

# Print results
print(f'Total Revenue from the Promotion: ${total_revenue:.2f}')

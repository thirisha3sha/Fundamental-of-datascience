"""Scenario: You are managing inventory for a bookstore and need to calculate the total cost of a customer's purchase, including discounts and taxes. You have lists item_prices and quantities where each element corresponds to the price and quantity of an item purchased. The discount rate and tax rate are given as percentages.
Question: Use arithmetic operations to calculate the total cost of a customer's purchase, considering the discounts and taxes based on the item prices, quantities, discount rate, and tax rate."""
import pandas as pd
# Discount rate and tax rate (as percentages)
discount_rate = 10  # 10% discount
tax_rate = 8  # 8% tax

# Create a DataFrame to organize the data
data = {
    'Item Price':[25.0, 15.0, 10.0, 30.0] ,
    'Quantity':[2, 3, 1, 2] 
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Calculate total cost before discounts and taxes
df['Total Cost'] = df['Item Price'] * df['Quantity']

# Calculate total discount
total_discount = df['Total Cost'].sum() * (discount_rate / 100)

# Apply discount to get discounted total cost
df['Discounted Cost'] = df['Total Cost'] - total_discount

# Calculate total tax
total_tax = df['Discounted Cost'].sum() * (tax_rate / 100)

# Calculate final total cost including taxes
total_cost_with_tax = df['Discounted Cost'].sum() + total_tax

# Display the results
print(f"Total cost before discounts and taxes: ${df['Total Cost'].sum():.2f}")
print(f"Total discount applied: ${total_discount:.2f}")
print(f"Discounted cost after discount: ${df['Discounted Cost'].sum():.2f}")
print(f"Total tax applied: ${total_tax:.2f}")
print(f"Total cost including taxes: ${total_cost_with_tax:.2f}")



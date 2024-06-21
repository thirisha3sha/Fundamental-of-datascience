""" Scenario: You are a cashier at a grocery store and need to calculate the total cost of a customer's purchase, including applicable discounts and taxes.
You have the item prices and quantities in separate lists, and the discount and tax rates are given as percentages. Your task is to calculate the total cost for the customer.
Question: Use arithmetic operations to calculate the total cost of a customer's purchase, including discounts and taxes, given the item prices, quantities, discount rate, and tax rate?
"""
import pandas as pd
data={
    'price':[10.0, 20.0, 15.0],
    'quantities':[2,1,3]
    }
df=pd.DataFrame(data)
discount_rate=10
tax_rate=8
print("dataset preview:\n",df)
df['subtotal']=df['price']*df['quantities']
total_subtotal=df['subtotal'].sum()
discount_amount=total_subtotal*(discount_rate/100)
subtotal_after_discount=total_subtotal-discount_amount
tax_amount=subtotal_after_discount*(tax_rate/100)
total_cost=subtotal_after_discount+tax_amount
print("Subtotal:", total_subtotal)
print("Discount Amount:", discount_amount)
print("Subtotal after Discount:", subtotal_after_discount)
print("Tax Amount:", tax_amount)
print("Total Cost:", total_cost)

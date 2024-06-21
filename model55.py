"""Scenario : You are a data scientist working for a company that sells products online. You
have been tasked with creating a simple plot to show the sales of a product over time.
Question:
1. Write code to create a simple line plot in Python using Matplotlib to predict sales happened
in a month?
2. Write code to create a scatter plot in Python using Matplotlib to predict sales happened in a
month?
3. Develop a Python program to create a bar plot of the monthly sales data."""
import matplotlib.pyplot as plt
import pandas as pd

# Sample sales data for a month
data = {
    'Day': range(1, 31),
    'Sales': [100, 150, 130, 170, 160, 190, 200, 210, 180, 220,
              230, 240, 250, 260, 270, 280, 290, 300, 310, 320,
              330, 340, 350, 360, 370, 380, 390, 400, 410, 420]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Sales Over a Month - Line Plot')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Day'], df['Sales'], color='r')
plt.title('Sales Over a Month - Scatter Plot')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(df['Day'], df['Sales'], color='skyblue')
plt.title('Sales Over a Month - Bar Plot')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

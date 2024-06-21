"""13.Scenario: You are a data analyst working for a company that sells products online. You
have been tasked with analyzing the sales data for the past month. The data is stored in a
Pandas data frame.
Question: Develop a code in python to find the frequency distribution of the ages of the
customers who have made a purchase in the past month."""
import pandas as pd

# Sample data (assuming 'age' column exists in the DataFrame)
data = {
    'customer_id': [1, 2, 3, 4, 5],
    'age': [30, 25, 35, 28, 40],  # Example ages of customers
    'purchase_date': ['2023-05-01', '2023-05-03', '2023-05-05', '2023-05-07', '2023-05-10']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'purchase_date' to datetime format
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# Filter customers who made a purchase in the past month (assuming 'purchase_date' is within the past month)
current_month = df['purchase_date'].dt.month.max()  # Get the month of the latest purchase
filtered_data = df[df['purchase_date'].dt.month == current_month]

# Calculate frequency distribution of ages
age_distribution = filtered_data['age'].value_counts().sort_index()

# Print the frequency distribution
print("Frequency distribution of ages of customers who made a purchase in the past month:")
print(age_distribution)

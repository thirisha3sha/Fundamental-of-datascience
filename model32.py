"""You are a data scientist working in a retail analytics firm. Your team wants to analyze customer purchase behavior to optimize product placement and promotions.
Your task is to apply market basket analysis to identify which products are frequently bought together by customers. Write Python code to load the transaction data,
 preprocess it, mine frequent itemsets, and generate association rules to understand customer purchasing patterns.
"""
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample transaction data: list of transactions, each containing a list of purchased products
data = {
    'TransactionID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Items': [
        ['Milk', 'Bread', 'Butter'],
        ['Bread', 'Butter', 'Cheese'],
        ['Milk', 'Bread'],
        ['Bread', 'Butter'],
        ['Milk', 'Butter'],
        ['Bread', 'Cheese'],
        ['Milk', 'Bread', 'Cheese'],
        ['Milk', 'Cheese'],
        ['Butter', 'Cheese'],
        ['Milk', 'Bread', 'Butter', 'Cheese']
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Preprocess the data: Convert transactions into a one-hot encoded DataFrame
one_hot = df['Items'].str.join('|').str.get_dummies()
df_one_hot = pd.concat([df['TransactionID'], one_hot], axis=1).groupby('TransactionID').sum()

# Mine frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(df_one_hot, min_support=0.3, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules)

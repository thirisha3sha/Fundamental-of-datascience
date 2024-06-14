import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree

# Creating a sample sales dataset
sales_data = pd.DataFrame({
    'Promotions': [100, 200, 150, 300, 250],
    'Advertising_Expenditure': [200, 300, 250, 350, 400],
    'Seasonal_Trends': [0.1, 0.2, 0.15, 0.25, 0.3],
    'Sales': [500, 600, 550, 700, 650]
})

# Splitting into features and target variable
X = sales_data.drop('Sales', axis=1)
y = sales_data['Sales']

# Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Visualization - Decision Tree
plt.figure(figsize=(10, 8))
plot_tree(model, feature_names=X.columns, filled=True, rounded=True)
plt.title('Decision Tree for Sales Prediction')
plt.show()

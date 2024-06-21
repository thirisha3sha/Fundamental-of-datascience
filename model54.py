"""Scenario: You work for a real estate agency and have been given a dataset containing
information about properties for sale. The dataset is stored in a Pandas DataFrame named
property_data. The DataFrame has columns for property ID, location, number of
bedrooms, area in square feet, and listing price. Your task is to analyze the data and answer
specific questions about the properties.
Question: Using Pandas DataFrame operations, how would you find the following
information from the property_data DataFrame:
1. The average listing price of properties in each location.
2. The number of properties with more than four bedrooms.
3. The property with the largest area."""
import pandas as pd

# Sample data
data = {
    'property_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb', 'Rural', 'Rural', 'Suburb', 'Downtown', 'Rural', 'Downtown'],
    'bedrooms': [3, 4, 2, 5, 4, 3, 5, 2, 6, 3],
    'area_sqft': [1500, 2000, 800, 2200, 1800, 1600, 2100, 850, 2500, 1300],
    'listing_price': [300000, 400000, 200000, 450000, 350000, 320000, 420000, 180000, 480000, 280000]
}

# Create DataFrame
property_data = pd.DataFrame(data)

# Display the DataFrame
print("Property DataFrame:")
print(property_data)

# Average listing price of properties in each location
average_listing_price_by_location = property_data.groupby('location')['listing_price'].mean().reset_index()
print("\nAverage listing price of properties in each location:")
print(average_listing_price_by_location)

# Number of properties with more than four bedrooms
properties_more_than_four_bedrooms = property_data[property_data['bedrooms'] > 4].count()
print("\nNumber of properties with more than four bedrooms:")
print(properties_more_than_four_bedrooms['property_id'])

# Property with the largest area
property_with_largest_area = property_data.loc[property_data['area_sqft'].idxmax()]
print("\nProperty with the largest area:")
print(property_with_largest_area)

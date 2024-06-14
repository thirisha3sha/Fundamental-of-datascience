"""Scenario: You work for a real estate agency and have been given a dataset containing information about properties for sale. The dataset is stored in a Pandas DataFrame named property_data. The DataFrame has columns for property ID, location, number of bedrooms, area in square feet, and listing price. Your task is to analyze the data and answer specific questions about the properties.
Question: Using Pandas DataFrame operations, how would you find the following information from the property_data DataFrame:
The average listing price of properties in each location.
The number of properties with more than four bedrooms.
The property with the largest area."""
import pandas as pd
data={'property_id':[1,2,3,4,5],
      'location':['aaa','bbb','vvv','mmm','vccc'],
      'bedrooms':[3,4,2,5,5],
      'area_sqft':[1500,1355,1200,3000,2900],
      'listing_price':[300000,450000,200000,500000,450000]
      }
property_data=pd.DataFrame(data)
avg_price_by_location=property_data.groupby('location')['listing_price'].mean()
num_properties_more_than_four_bedrooms=property_data[property_data['bedrooms']>4].shape[0]
property_with_largest_area=property_data.loc[property_data['area_sqft'].idxmax()]
print("\nnumber of properties more than 4 bedrroms:",num_properties_more_than_four_bedrooms)
print("\naverage listing proce of properties in each loaction:\n",avg_price_by_location)
print("\nproperty with the largest area:\n",property_with_largest_area)

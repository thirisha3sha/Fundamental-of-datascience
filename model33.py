  """Scenario: You are a climate scientist analyzing climate data from multiple weather stations across different regions. The dataset contains daily temperature readings for each station over the past year.
Calculate the average daily temperature for each weather station to understand regional climate patterns.
Compute the standard deviation of daily temperatures for each station to assess temperature variability.
Identify the weather station with the widest temperature range (difference between the highest and lowest temperatures) to study climate extremes.
Determine the weather station with the most stable temperatures, indicated by the lowest standard deviation, to assess consistency in climate conditions
"""
import pandas as pd
import numpy as np

# Sample data: Daily temperature readings for each weather station over the past year (365 days)
np.random.seed(0)  # For reproducibility
stations = ['Station_A', 'Station_B', 'Station_C', 'Station_D']
data = {
    'Date': pd.date_range(start='2023-01-01', periods=365).tolist() * len(stations),
    'Station': np.repeat(stations, 365),
    'Temperature': np.concatenate([
        np.random.normal(loc=15, scale=5, size=365),  # Station_A
        np.random.normal(loc=20, scale=6, size=365),  # Station_B
        np.random.normal(loc=10, scale=4, size=365),  # Station_C
        np.random.normal(loc=25, scale=7, size=365)   # Station_D
    ])
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the average daily temperature for each weather station
avg_temps = df.groupby('Station')['Temperature'].mean().reset_index()
avg_temps.columns = ['Station', 'AverageTemperature']

# Compute the standard deviation of daily temperatures for each station
std_devs = df.groupby('Station')['Temperature'].std().reset_index()
std_devs.columns = ['Station', 'TemperatureStdDev']

# Identify the weather station with the widest temperature range (difference between the highest and lowest temperatures)
temp_ranges = df.groupby('Station')['Temperature'].agg(lambda x: x.max() - x.min()).reset_index()
temp_ranges.columns = ['Station', 'TemperatureRange']

# Determine the weather station with the most stable temperatures (lowest standard deviation)
most_stable_station = std_devs.loc[std_devs['TemperatureStdDev'].idxmin()]

# Merge results into a single DataFrame for easy viewing
results = pd.merge(avg_temps, std_devs, on='Station')
results = pd.merge(results, temp_ranges, on='Station')

# Display the results
print("Average Daily Temperature, Standard Deviation, and Temperature Range for each Weather Station:")
print(results)

print("\nWeather Station with the Widest Temperature Range:")
print(temp_ranges.loc[temp_ranges['TemperatureRange'].idxmax()])

print("\nWeather Station with the Most Stable Temperatures (Lowest Standard Deviation):")
print(most_stable_station)

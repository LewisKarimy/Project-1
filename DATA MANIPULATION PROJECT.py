#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #importing necessary libraries
import numpy as nm #importing the necessary libraries


# In[2]:


df = pd.read_csv("E:/e - book/Tech/Python/1. Weather Data.csv") # importing the csv file


# In[3]:


print(df) #printing the total number of rows and columns


# In[4]:


print(df.head(10)) #printing the first ten rows of the csv file


# In[5]:


print(df.tail(10)) #prints the last 10 rows of the csv file


# In[33]:


#Find all records where the weather was exactly clear.
def find_clear_weather(df):
    # Check if 'Weather' column exists
    if 'Weather' not in df.columns:
        print("'Weather' column not found in the DataFrame.")
        return
    
    # Find rows where the 'Weather' column is equal to 'clear'
    clear_rows = df[df['Weather'].str.lower() == 'clear']
    
    # Print results
    if not clear_rows.empty:
        print("Rows where 'Weather' is 'clear':")
        for index, row in clear_rows.iterrows():
            print(f"Row {index + 2}: {row.to_dict()}")  # +2 because DataFrame index starts at 0 and we account for header row
    else:
        print("No rows found where 'Weather' is 'clear'.")
    
    clear_count = len(clear_rows)
    print(f"Total number of rows where 'Weather' is 'clear': {clear_count}")        
        

# Assuming the DataFrame is already created and named 'df'
# If not, uncomment the following line and replace 'your_file.csv' with your actual file name
# df = pd.read_csv('your_file.csv')

find_clear_weather(df)


# In[6]:


#Find the number of times the wind speed was exactly 4 km/h
count = (df['Wind Speed_km/h'] == 4).sum()
print(f"The wind speed was exactly 4 km/h {count} times.")


# In[7]:


#Check if there are any NULL values present in the dataset.
null_check = df.isnull().sum()
print("Number of NULL values in each column:")
print(null_check)

if null_check.sum() > 0:
    print("\nThere are NULL values present in the dataset.")
else:
    print("\nThere are no NULL values in the dataset.")


# In[8]:


# Rename the column "Weather" to ""Weather_Condition"
df = df.rename(columns={'Weather': 'Weather_Condition'})
print(df.columns)


# In[10]:


# What is the mean visibility of the dataset
mean_visibility = df['Visibility_km'].mean()
print(f"The mean visibility is {mean_visibility:.2f} km")


# In[11]:


# Find the number of records where the wind speed is greater than 24 km/hr and visibility is equal to 25 km.
count = ((df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)).sum()
print(f"Number of records with wind speed > 24 km/h and visibility = 25 km: {count}")


# In[13]:


# What is the mean value of each column for each weather condition

columns_of_interest = ['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km','Press_kPa']
mean_by_weather = df.groupby('Weather_Condition')[columns_of_interest].mean()
print(mean_by_weather)


# In[20]:


#Find all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40.
result = df[
    ((df['Weather_Condition'] == 'Clear') & (df['Rel Hum_%'] > 50)) |
    (df['Visibility_km'] > 40)
    ]

print(f"Number of instances found: {len(result)}")
print("\nFirst few rows of the result:")
print(result.head())


# In[22]:


# Find the number of weather conditions that include snow
snow_conditions = df['Weather_Condition'].str.contains('snow', case=False, na=False)
num_snow_conditions = snow_conditions.sum()

print(f"Number of weather conditions including snow: {num_snow_conditions}")



# In[ ]:





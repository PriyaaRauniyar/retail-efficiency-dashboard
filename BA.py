"""
BA.py - Data Cleaning Script for Retail Operational Data
Author: Priya Rauniyar
Description:
This script loads a retail dataset, performs basic data cleaning and feature engineering,
calculates new metrics (Total_Time, Is_Efficient), and exports a cleaned file
for further analysis in Power BI.
"""
# Import necessary libraries
import pandas as pd

# Load the Excel file
df = pd.read_excel("Retail_Store_Operational_Data.xlsx")

# Create new column 'Total_Time' by summing processing and wait times
df['Total_Time'] = df['Order_Processing_Time'] + df['Customer_Wait_Time']

# Create new column 'Is_Efficient' - flag orders completed under 25 minutes
df['Is_Efficient'] = df['Total_Time'] < 25

# Save the cleaned data to a new Excel file
df.to_excel("Cleaned_Retail_Operational_Data.xlsx", index=False)

# Optional: Display first few rows for confirmation
print(df.head())

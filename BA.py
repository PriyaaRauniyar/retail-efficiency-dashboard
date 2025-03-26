import pandas as pd

# Load your Excel file
df = pd.read_excel("Retail_Store_Operational_Data.xlsx")

# Show the first 5 rows
print(df.head())
# Convert 'Order_Date' to datetime format
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Create 'Total_Time' column
df['Total_Time'] = df['Order_Processing_Time'] + df['Customer_Wait_Time']

# Create 'Is_Efficient' column (True if processing time ≤ 15 mins)
df['Is_Efficient'] = df['Order_Processing_Time'] <= 15

# Filter out Cancelled orders
df_cleaned = df[df['Order_Status'] != 'Cancelled']

# Show the cleaned data
print(df_cleaned.head())
df_cleaned.to_excel("Cleaned_Retail_Operational_Data.xlsx", index=False)

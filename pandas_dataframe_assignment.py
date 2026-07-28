"""
Pandas Dataframe - Assignment
Pwskills

Dataset: retail_dataset_.csv
(Place this file in the same directory as this script.)

NOTE: The provided dataset uses "Product Category" (not "Product") and has
no direct "Sales" column, so Sales is derived as Quantity x Price to match
the assignment's terminology. Q1 uses its own independent sample data with
the exact column names requested (Product, Region, Sales, Quantity).
"""

import pandas as pd

CSV_PATH = "retail_dataset_.csv"


# ---------------------------------------------------------------------------
# Q1. Creating a DataFrame
# Create a Pandas DataFrame using a Python dictionary with the columns:
# Product, Region, Sales, Quantity. Add at least 5 rows of sample data.
# ---------------------------------------------------------------------------
sample_data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Region": ["North", "South", "East", "West", "North"],
    "Sales": [50000, 30000, 20000, 15000, 5000],
    "Quantity": [5, 10, 8, 6, 20]
}
sample_df = pd.DataFrame(sample_data)

print("Q1: Sample DataFrame")
print(sample_df)


# ---------------------------------------------------------------------------
# Load dataset for Q2-Q10
# ---------------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)
df['Sales'] = df['Quantity'] * df['Price']


# ---------------------------------------------------------------------------
# Q2. Data Inspection
# ---------------------------------------------------------------------------
print("\nQ2: First 5 rows")
print(df.head())

print("\nQ2: Last 5 rows")
print(df.tail())

print("\nQ2: Dataset info")
print(df.info())

print("\nQ2: Dataset shape")
print(df.shape)


# ---------------------------------------------------------------------------
# Q3. Column Selection
# Select and display Product, Region, Sales columns.
# ---------------------------------------------------------------------------
print("\nQ3: Product, Region, Sales columns")
print(df[['Product Category', 'Region', 'Sales']])


# ---------------------------------------------------------------------------
# Q4. Indexing using .loc
# ---------------------------------------------------------------------------
print("\nQ4: Row with index 10")
print(df.loc[10])

print("\nQ4: Sales value at index 20")
print(df.loc[20, 'Sales'])


# ---------------------------------------------------------------------------
# Q5. Indexing using .iloc
# ---------------------------------------------------------------------------
print("\nQ5: First 6 rows, first 4 columns")
print(df.iloc[0:6, 0:4])

print("\nQ5: Sales value from the 3rd row")
print(df.iloc[2]['Sales'])


# ---------------------------------------------------------------------------
# Q6. Row Slicing
# ---------------------------------------------------------------------------
print("\nQ6: First 10 rows")
print(df.iloc[:10])

print("\nQ6: Rows 15 to 25")
print(df.iloc[15:26])


# ---------------------------------------------------------------------------
# Q7. Filtering Data
# ---------------------------------------------------------------------------
print("\nQ7: Rows where Region = East")
print(df[df['Region'] == 'East'])

print("\nQ7: Rows where Sales > 1500")
print(df[df['Sales'] > 1500])


# ---------------------------------------------------------------------------
# Q8. Multiple Condition Filtering
# ---------------------------------------------------------------------------
print("\nQ8: Rows where Region is West AND Sales > 1200")
print(df[(df['Region'] == 'West') & (df['Sales'] > 1200)])


# ---------------------------------------------------------------------------
# Q9. Descriptive Statistics
# ---------------------------------------------------------------------------
print("\nQ9: describe() summary statistics")
print(df.describe())

print("\nQ9: Mean sales value:", df['Sales'].mean())
print("Q9: Maximum quantity sold:", df['Quantity'].max())
print("Q9: Minimum sales value:", df['Sales'].min())


# ---------------------------------------------------------------------------
# Q10. Aggregation Analysis
# ---------------------------------------------------------------------------
print("\nQ10: Total sales:", df['Sales'].sum())
print("Q10: Average sales:", df['Sales'].mean())
print("Q10: Maximum sales:", df['Sales'].max())
print("Q10: Minimum sales:", df['Sales'].min())

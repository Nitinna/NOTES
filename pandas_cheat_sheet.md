Here's a concise Pandas cheat sheet to help you with common tasks:

---

## **Basics**
```python
import pandas as pd
import numpy as np
```

### **Creating DataFrames**
```python
# From dictionary
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# From NumPy array
df = pd.DataFrame(np.random.rand(4, 3), columns=['A', 'B', 'C'])

# From CSV
df = pd.read_csv('file.csv')

# From Excel
df = pd.read_excel('file.xlsx')
```

---

## **Viewing Data**
```python
df.head(n=5)        # First 5 rows
df.tail(n=5)        # Last 5 rows
df.shape            # (rows, columns)
df.info()           # Data types and non-null counts
df.describe()       # Summary statistics
df.columns          # List of column names
df.index            # Row index
```

---

## **Selecting Data**
```python
# Single column
df['A']            # Returns Series
df[['A', 'B']]     # Returns DataFrame

# Rows
df.iloc[0]         # First row by position
df.loc[0]          # First row by index label

# Subset
df.iloc[0:3, 1:4]  # Rows 0-2, columns 1-3
df.loc[0:3, ['A']] # Rows 0-3, column 'A'
```

---

## **Filtering & Conditional Selection**
```python
df[df['A'] > 2]               # Filter rows where column A > 2
df[(df['A'] > 2) & (df['B'] < 5)]  # Multiple conditions
df.query('A > 2 and B < 5')   # Query syntax
```

---

## **Modifying Data**
```python
df['C'] = df['A'] + df['B']          # Add new column
df.rename(columns={'A': 'Alpha'}, inplace=True)  # Rename column
df.drop('A', axis=1, inplace=True)  # Drop column
df.drop([0, 1], axis=0, inplace=True)  # Drop rows
df['A'] = df['A'].astype(float)      # Change data type
```

---

## **Handling Missing Data**
```python
df.isna()                    # Check for NaNs
df.isna().sum()              # Count NaNs in each column
df.dropna()                  # Drop rows with NaNs
df.fillna(value=0, inplace=True)  # Replace NaNs with 0
```

---

## **Aggregation & Grouping**
```python
df.sum()                     # Column-wise sum
df['A'].mean()               # Mean of column A
df.groupby('B').mean()       # Group by column B, take mean
df.groupby(['B', 'C']).sum() # Multi-level groupby
```

---

## **Sorting**
```python
df.sort_values('A')          # Sort by column A
df.sort_values(['A', 'B'], ascending=[True, False])  # Multi-column sort
df.sort_index()              # Sort by index
```

---

## **Merging Data**
```python
# Concatenate
pd.concat([df1, df2], axis=0) # Append rows
pd.concat([df1, df2], axis=1) # Combine columns

# Merge (joins)
pd.merge(df1, df2, on='key')        # Inner join
pd.merge(df1, df2, how='left')     # Left join
```

---

## **Saving Data**
```python
df.to_csv('file.csv', index=False)    # Save as CSV
df.to_excel('file.xlsx', index=False) # Save as Excel
```

Would you like me to include advanced topics like time-series handling or pivot tables?
Here is the content converted to Markdown format in Hinglish:

```markdown
# Pandas Operations Guide

### Copying DataFrames
```python
df1 = df  # Yeh df ka reference banaega
df1 = df.copy()  # Yeh df ka copy banaega
```

### Ignoring Header in CSV
Agar aap nahi chahte ki pehli row header ke roop mein treat ho:
```python
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
```

### Checking Current Columns
```python
df.columns  # Columns ke naam dekhne ke liye
```

### Renaming Columns
```python
df.columns = ['sl', 'sw', 'pl', 'pw', 'flower_type']  # Columns ke naam ko rename karna
```

### Quick DataFrame Analysis
```python
df.describe()  # Numerical columns ke liye summary statistics dega
```

### Accessing Columns
```python
df.sl  # 'sl' column ko access karna
df['sl']  # Dusra method column ko access karne ka
```

### Checking for NULL Values
```python
df.isnull()  # Missing values ko check karne ke liye
df.isnull().sum()  # Har column mein missing values ka count
```

### Accessing Rows and Columns with `iloc` and `loc`

- **iloc (Integer Location):** Integer positions ke basis pe kaam karta hai
```python
df.iloc[0]  # Pehla row
df.iloc[0, 1]  # Pehla row, doosra column
df.iloc[:3]  # Pehle 3 rows
```

- **loc (Label Location):** Labels ke basis pe kaam karta hai
```python
df.loc['row1']  # Label ke basis pe row ko get karna
df.loc['row1', 'column2']  # Specific row aur column ke value ko get karna
df.loc[df['column1'] > 10]  # Un rows ko get karna jahan column1 ki value > 10 ho
```

### Example with a Student Table:
```text
Name     Math  English
Alice    90    85
Bob      78    92
Charlie  88    79
```

**Using `iloc`:**
```python
df.iloc[1, 2]  # Output: "92"
```

**Using `loc`:**
```python
df.loc['Bob', 'English']  # Output: "92"
```

### Removing Duplicate Rows
```python
df = df.drop_duplicates()  # Duplicate rows ko remove karna
df = df.drop_duplicates(subset=['column1', 'column2'])  # Specific columns ke basis pe duplicates ko remove karna
df = df.drop_duplicates(keep='last')  # Last occurrence ko rakhe, baaki remove kare
df = df.drop_duplicates(keep=False)  # Sare duplicates ko hata de
df.duplicated().sum()  # Duplicate rows ka count
df['column_name'].duplicated().sum()  # Specific column mein duplicates ka count
```

### Data Sampling
```python
sample = df.sample(n=5)  # 5 random rows milega
sample = df.sample(frac=0.3)  # 30% random rows milega
sample = df.sample(n=5, replace=True)  # Rows ka duplicate bhi aa sakta hai
sample = df.sample(n=5, weights='A')  # Weighted random sampling, 'A' wale rows zyada pick honge
sample = df.sample(n=5, random_state=42)  # Har baar same sample milega
sample = df.sample(n=1, axis=1)  # 1 random column milega
```

### Reading CSV Files
```python
df = pd.read_csv('data.csv')  # CSV file ko DataFrame mein load karna
df = pd.read_csv('data.tsv', sep='\t')  # Tab-separated file ko load karna
df = pd.read_csv('data.csv', usecols=['A', 'B'])  # Sirf 'A' aur 'B' columns ko load karna
df = pd.read_csv('data.csv', header=None, names=['Col1', 'Col2', 'Col3'])  # Custom column names ke saath load karna
df = pd.read_csv('data.csv', index_col='ID')  # 'ID' column ko index banaana
df = pd.read_csv('data.csv', skiprows=2)  # Pehli 2 rows skip karke file ko read karna
df = pd.read_csv('data.csv', encoding='utf-8')  # UTF-8 encoding ke saath file ko load karna
```

### Resetting Index
```python
df.reset_index(level=1)  # MultiIndex ke case mein specific level ko reset karna
df.reset_index(drop=True)  # Index ko reset karke purana index hata dena
df.reset_index(inplace=True)  # Original DataFrame ko modify karna, naya DataFrame return nahi karega
```

### DataFrame Filtering Methods

- **Boolean Indexing:**
```python
filtered_df = df[df['Age'] > 30]  # Filter rows jahan Age > 30 ho
filtered_df = df[(df['Age'] > 25) & (df['Name'] == 'Bob')]  # Filter rows jahan Age > 25 aur Name 'Bob' ho
```

- **Using `query()`:**
```python
filtered_df = df.query('Age > 30')  # Filter rows jahan Age > 30 ho
filtered_df = df.query('Age > 25 and Name == "Bob"')  # Filter rows jahan Age > 25 aur Name 'Bob' ho
```

- **Using `loc[]`:**
```python
filtered_df = df.loc[df['Age'] > 30]  # Filter rows jahan Age > 30 ho
filtered_df = df.loc[df['Age'] > 25, 'Name']  # Filter rows jahan Age > 25 ho aur sirf 'Name' column ko select karna
```

- **Using `isin()`:**
```python
filtered_df = df[df['Name'].isin(['Alice', 'Charlie'])]  # Filter rows jahan Name 'Alice' ya 'Charlie' ho
```

- **Using `between()`:**
```python
filtered_df = df[df['Age'].between(25, 30)]  # Filter rows jahan Age 25 aur 30 ke beech ho (inclusive)
```

### Adding and Removing Columns
```python
df['C'] = df['A'] * 2  # 'A' column ko 2 se multiply karke new column 'C' add karna
df['D'] = df['A'].apply(lambda x: x + 10)  # Lambda function use karke column 'A' ko modify karna
df = df.drop('B', axis=1)  # Column 'B' ko remove karna
df = df.rename(columns={'A': 'Alpha', 'B': 'Beta'})  # Column names ko rename karna
```

### Handling NaN Values
```python
df.isna()  # NaN values ko check karne ke liye
df.isna().sum()  # Har column mein NaN values ka count
df_cleaned_rows = df.dropna(axis=0)  # Rows ko drop karna jisme NaN ho
df_cleaned_cols = df.dropna(axis=1)  # Columns ko drop karna jisme NaN ho
df_cleaned_thresh = df.dropna(thresh=2, axis=0)  # Un rows ko drop karna jisme 2 se kam non-NaN values ho
df_filled_constant = df.fillna(0)  # NaN ko 0 se fill karna
df_filled_ffill = df.fillna(method='ffill')  # Forward fill NaN values
df_filled_bfill = df.fillna(method='bfill')  # Backward fill NaN values
df_filled_mean = df.fillna(df.mean())  # NaN ko mean se fill karna
```
```

This markdown file is in Hinglish, combining both Hindi and English for easier understanding.

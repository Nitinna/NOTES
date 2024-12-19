df1 = df

will act both same...if you want copy of df1...use below command

df1 = df.copy()

-------------------------

#Ignoring header -> If you don't want first row to be treated as a header, you can set header = None
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

-----------------------------
check current columns

df.columns
---------------------------------
To give particular name for columns

df.columns = ['sl', 'sw', 'pl', 'pw', 'flower_type']

-------------------------------------------

we can use describe() to quick analysis on df1

df.describe()
-----------------------------------------------
to look at a single column from the DataFrame

df.sl # here sl is column name

or second method to call any column from df

df['sl']
-----------------------------------------------
checking for NULL values

df.isnull()

if you want sum of null values in a particular column use this

df.isnull().sum()

---------------------------------------------------

In Pandas, iloc and loc are used to select and access rows and columns from a DataFrame or Series

iloc (Integer Location):- Works based on integer positions

Syntax: df.iloc[row_index, column_index]

example-

df.iloc[0] # Get the first row

df.iloc[0,1] # get the first row and second column

df.iloc[:3] # get the first 3 rows


==========================================

loc (Label Location):- Works based on labels

Syntax: df.loc[row_label, column_label]

df.loc['row1'] # get a row by its label

df.loc['row1' , 'column2'] # get a value from a specific row and coloumn

df.loc[df['column1'] > 10] # get all row where the value in a column matches a conditon

example both works flow
Imagine a table of students names and scores:
Name	Math	English
Alice	 90	     85
Bob	     78	     92
Charlie	 88	     79

iloc Example:

To get Bob English score:
df.iloc[1, 2]  # output - "92"

loc Example:

To get Bob English score:
df.loc['Bob', 'English'] # output - "92"

----------------------------------------------------------------------------------------------

Removing all duplicate rows

df = df.drop_duplicates()

df = df.drop_duplicates(subset=['column1', 'column2']) #Remove duplicates based on specific columns

df = df.drop_duplicates(keep='last') # df = df.drop_duplicates(keep='last')

df = df.drop_duplicates(keep=False) # Keep no duplicates (remove all duplicates)
 
df.duplicated().sum() # Count all duplicates (excluding the first occurrence)

df['column_name'].duplicated().sum() # Count duplicates in a specific column

 ------------------------------------------------------------------------------

Data sample method

Syntax:

DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)

sample = df.sample(n=5) # Output me 5 random rows milengi.

sample = df.sample(frac=0.3) # Ye 30% rows random return karega.

sample = df.sample(n=5, replace=True) # Iska matlab ek row multiple baar aa sakti hai.

sample = df.sample(n=5, weights='A') # Higher A values wali rows ka zyada chance hoga select hone ka.

sample = df.sample(n=5, random_state=42) # Har baar same sample milega.

sample = df.sample(n=1, axis=1) # Ek random column milega.


Notes:
1. Agar n aur frac dono na diye ho, to error aayega.
2. sample method original DataFrame ya Series ko modify nahi karta, balki ek nayi object return karta hai.

----------------------------------------------------------------------------------------------

read_csv method

pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, ...)

df = pd.read_csv('data.csv') # Puri CSV file ek DataFrame me load ho jayegi.

df = pd.read_csv('data.tsv', sep='\t') # Tab-separated file ka data ek DataFrame me load hoga.

df = pd.read_csv('data.csv', usecols=['A', 'B']) # Sirf A aur B columns load honge.

df = pd.read_csv('data.csv', header=None, names=['Col1', 'Col2', 'Col3']) # Custom column names ke saath file load hogi.

df = pd.read_csv('data.csv', index_col='ID') # ID column DataFrame ka index ban jayega.

df = pd.read_csv('data.csv', skiprows=2) # Puri file read hogi par pehli 2 rows skip ho jayengi.

df = pd.read_csv('data.csv', encoding='utf-8') # UTF-8 encoding ke saath file ka data load hoga.

----------------------------------------------------------------------------------------

df.reset_index() uses 

syntax:- DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')

df.reset_index(level=1)  # Sirf second level reset karega.(MultiIndex hone par, kaunsa level reset karna hai yeh specify karta hai. Agar None ho, toh saare levels reset ho jaayenge.)

df.reset_index(drop=True)  # Index hata kar sirf data rakhega.

df.reset_index(inplace=True)  # Agar True karenge, toh original DataFrame ko modify karega. Naya DataFrame return nahi karega.


Note:

Using only : =  df.reset_index():
'''
Resets the index and returns a new DataFrame.
The original DataFrame is unchanged unless you use inplace=True.
'''

------------------------------------------------------------------------------------------
Pandas data filtering methods 

1. Filtering with Boolean Indexing

filtered_df = df[df['Age'] > 30] # Filter rows where Age > 30

filtered_df = df[(df['Age'] > 25) & (df['Name'] == 'Bob')]  # Filter rows where Age > 25 AND Name is 'Bob'

Note:
Multiple Conditions
# Use logical operators (& for AND, | for OR, ~ for NOT):

filtered_df = df[~(df['Age'] == 25)] # Filter rows where Age is NOT 25

2. Filtering with query()

filtered_df = df.query('Age > 30') # Filter rows where Age > 30

filtered_df = df.query('Age > 25 and Name == "Bob"') # Filter rows where Age > 25 AND Name == 'Bob'

3. Filtering with .loc[]

filtered_df = df.loc[df['Age'] > 30] # Filter rows where Age > 30

filtered_df = df.loc[df['Age'] > 25, 'Name'] # Filter rows where Age > 25 and select only 'Name' column

4. Filtering with .iloc[]

filtered_df = df.iloc[:2] # Select the first two rows

filtered_df = df.iloc[:2, 0] # Select the first two rows and the first column

5. Filtering with .isin()
filtered_df = df[df['Name'].isin(['Alice', 'Charlie'])] # Filter rows where Name is in ['Alice', 'Charlie']

6. Filtering with .between()

filtered_df = df[df['Age'].between(25, 30)] # Filter rows where Age is between 25 and 30 (inclusive)

filtered_df = df[df['Name'].str.contains('li')] # Filter rows where Name contains 'li'

filtered_df = df[df['Name'].str.startswith('A')] # Filter rows where Name starts with 'A'

filtered_df = df.nlargest(2, 'Age') # Get top 2 rows with largest Age

filtered_df = df.nsmallest(2, 'Age') # Get top 2 rows with smallest Age

filtered_df = df[df['Age'].apply(lambda x: x % 2 == 0)] # Filter rows where Age is even

-------------------------------------------------------------------------------------------------------
adding and removing any column on df

df['C'] = df['A'] * 2  # New column 'C' is A multiplied by 2

df['D'] = df['A'].apply(lambda x: x + 10)  # Apply a lambda function to column 'A'

df = df.drop('B', axis=1)  # Removes column 'B'

df = df.drop(['A', 'C'], axis=1)  # Removes columns 'A' and 'C'

df = df.rename(columns={'A': 'Alpha', 'B': 'Beta'}) # ename columns using the rename() function

Adding a New Column Based on Existing Columns Using

df['E'] = df['Alpha'].apply(lambda x: 'High' if x > 5 else 'Low') # Using one column

df['F'] = df.apply(lambda row: row['Alpha'] + row['Beta'] if row['Alpha'] > 5 else row['Beta'], axis=1) # Using multiple columns


df.insert(1, 'G', [1, 2, 3])  # Inserts column 'G' at position 1

df = df.set_index('Alpha')  # Set 'Alpha' column as the index

Using lambda with Conditional Logic

df['G'] = df['Alpha'].apply(lambda x: 'Positive' if x > 0 else 'Negative') # perform conditional operations across columns or rows

df['H'] = df.apply(lambda row: row['Alpha'] * row['Beta'] if row['Alpha'] > 2 else row['Beta'], axis=1) #perform more complex operations using apply(), such as iterating over rows and applying custom logic

----------------------------------------------------------------------------------------------------------

handling nah in df 

df.isna()  # Ye ek boolean DataFrame return karega, jisme NaN values hain ya nahi

df.isna().sum() # Ye check karega ki kitni missing values har column mein hain

df_cleaned_rows = df.dropna(axis=0) #  Rows ko drop karte hain jinmein koi bhi NaN value ho

df_cleaned_cols = df.dropna(axis=1) # Columns ko drop karte hain jinmein koi bhi NaN value ho

df_cleaned_rows_all = df.dropna(how='all', axis=0) # Un rows ko drop karte hain jo pure NaN hain

df_cleaned_cols_all = df.dropna(how='all', axis=1) # Un columns ko drop karte hain jo pure NaN hain

df_cleaned_thresh = df.dropna(thresh=2, axis=0) # Drop karte hain wo rows jisme 2 se kam non-NaN values ho

df_filled_constant = df.fillna(0) # NaN ko ek constant value (0) se fill karte hain

df_filled_dict = df.fillna({'A': 0, 'B': 99, 'C': 5}) # NaN ko har column ke liye specific value se fill karte hain

df_filled_ffill = df.fillna(method='ffill') # NaN ko pichli valid value se fill karna (forward fill)

df_filled_bfill = df.fillna(method='bfill') # NaN ko next valid value se fill karna (backward fill)

df_filled_interpolated = df.interpolate() # NaN ko interpolation se fill karna

f_filled_mean = df.fillna(df.mean()) # NaN ko har column ke mean se fill karte hain

df_filled_median = df.fillna(df.median()) # NaN ko har column ke median se fill karte hain

# NaN ko har column ke mode se fill karte hain
df_filled_mode = df.fillna(df.mode().iloc[0])  # Mode ek DataFrame return karta hai, isliye `.iloc[0]` use karte hain

# NaN ko custom logic se replace karte hain (for example, 10 se multiply karte hain)
df_filled_custom = df.apply(lambda col: col.fillna(col.mean()) if col.name == 'A' else col.fillna(0), axis=0)

# Column 'A' ke NaN ko us column ke mean se fill karte hain
df['A'] = df['A'].fillna(df['A'].mean())

# Column 'B' mein se NaN ko drop karte hain
df['B'] = df['B'].dropna()

# Check karte hain ki DataFrame mein missing values hain ya nahi
print(df.isnull().sum())  # Har column mein kitni NaN values hain, wo count karte hain


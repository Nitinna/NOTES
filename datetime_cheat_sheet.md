Here’s a comprehensive cheat sheet for Python's `datetime` library:

---

### **Importing**
```python
from datetime import datetime, date, time, timedelta
import calendar
```

---

### **Current Date and Time**
```python
# Current datetime
now = datetime.now()

# Current date
today = date.today()

# Current time
current_time = datetime.now().time()
```

---

### **Creating Specific Dates and Times**
```python
# Specific date
specific_date = date(2024, 12, 20)

# Specific time
specific_time = time(15, 30, 0)  # 3:30 PM

# Specific datetime
specific_datetime = datetime(2024, 12, 20, 15, 30, 0)
```

---

### **Formatting Dates and Times**
```python
# Convert datetime to string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Format codes:
# %Y - Full year (2024)
# %m - Month as a number (01-12)
# %d - Day of the month (01-31)
# %H - Hour (24-hour)
# %I - Hour (12-hour)
# %M - Minute (00-59)
# %S - Second (00-59)
# %p - AM/PM
# %A - Full weekday name (e.g., Monday)
# %B - Full month name (e.g., December)
```

---

### **Parsing Strings to datetime**
```python
date_string = "2024-12-20 15:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
```

---

### **Arithmetic with Dates**
```python
# Add or subtract days
future_date = today + timedelta(days=10)
past_date = today - timedelta(days=5)

# Add or subtract hours
future_time = now + timedelta(hours=5)
past_time = now - timedelta(hours=5)
```

---

### **Extracting Components**
```python
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
weekday = now.weekday()  # Monday = 0, Sunday = 6
iso_weekday = now.isoweekday()  # Monday = 1, Sunday = 7
```

---

### **Comparison**
```python
if date(2024, 12, 25) > today:
    print("Christmas is coming!")
```

---

### **Difference Between Dates**
```python
delta = date(2025, 1, 1) - today
print(delta.days)  # Days until the new year

# Total seconds between two datetimes
delta_seconds = (datetime(2025, 1, 1) - now).total_seconds()
print(delta_seconds)
```

---

### **Working with Timezones**
```python
from datetime import timezone, timedelta

# UTC time
utc_now = datetime.now(timezone.utc)

# Adding a timezone offset
offset = timezone(timedelta(hours=5, minutes=30))  # IST
ist_time = now.replace(tzinfo=offset)
```

---

### **Calendar Functions**
```python
# Check if a year is a leap year
is_leap = calendar.isleap(2024)  # True

# Get the calendar for a specific month
print(calendar.month(2024, 12))

# Get the calendar for a specific year
print(calendar.calendar(2024))
```

---

### **Handling Epoch Time**
```python
# From timestamp
timestamp = 1700000000
date_from_timestamp = datetime.fromtimestamp(timestamp)

# To timestamp
timestamp_from_date = now.timestamp()
```

---

### **ISO Format**
```python
# Convert to ISO format
iso_format = now.isoformat()

# Parse from ISO format
parsed_iso = datetime.fromisoformat(iso_format)
```

---


Pandas mein datetime series ke saath kaafi useful operations kar sakte hain, jo time series data ke saath kaam karte waqt kaafi madadgar hote hain. Yeh kuch common operations hain jo aap pandas mein perform kar sakte hain:

### 1. **Datetime ko `datetime` Type Mein Convert Karna**
Agar aapke paas date strings hain aur aap unhe `datetime` type mein convert karna chahte hain, toh aap `pd.to_datetime()` ka use kar sakte hain:
```python
import pandas as pd

# Example data
data = {'dates': ['2025-01-01', '2025-01-02', '2025-01-03']}
df = pd.DataFrame(data)

# Convert to datetime
df['dates'] = pd.to_datetime(df['dates'])
```

### 2. **Date/Time Components Nikaalna**
Datetime series ke saath aap year, month, day, hour, minute, second, etc. easily extract kar sakte hain:
```python
# Extract components
df['year'] = df['dates'].dt.year
df['month'] = df['dates'].dt.month
df['day'] = df['dates'].dt.day
df['hour'] = df['dates'].dt.hour
df['minute'] = df['dates'].dt.minute
df['second'] = df['dates'].dt.second
```

### 3. **Datetime Index Set Karna**
Datetime column ko DataFrame ka index banane ke liye `.set_index()` ka use kar sakte hain:
```python
df.set_index('dates', inplace=True)
```

### 4. **Resampling**
Aap data ko kisi specific frequency (jaise daily, monthly) pe resample kar sakte hain using `.resample()` method:
```python
# Resample to daily frequency and take the mean
df_resampled = df.resample('D').mean()
```

### 5. **Time Shifting**
Aap datetime series ko shift kar sakte hain (positive for future, negative for past) using `.shift()` method:
```python
# Shift data by 1 day forward
df['shifted'] = df['dates'].shift(1, freq='D')
```

### 6. **Date Range Generate Karna**
Agar aapko specific range ke dates generate karne hain, toh `pd.date_range()` use kar sakte hain:
```python
# Generate a date range
date_range = pd.date_range('2025-01-01', periods=5, freq='D')
```

### 7. **Time Differences**
Aap datetime objects ke beech ka time difference nikaal sakte hain:
```python
# Example data
df2 = pd.DataFrame({'dates': ['2025-01-02', '2025-01-04']})
df2['dates'] = pd.to_datetime(df2['dates'])

# Time difference
df['time_diff'] = df2['dates'] - df['dates']
```

### 8. **Date Arithmetic**
Datetime objects ke saath arithmetic operations perform kar sakte hain, jaise ki time add ya subtract karna:
```python
# Add 1 day to the datetime column
df['new_date'] = df['dates'] + pd.Timedelta(days=1)
```

### 9. **Date ke Basis Pe Filter Karna**
Datetime column ke basis pe aap specific dates ko filter kar sakte hain:
```python
# Filter by a specific year
df_filtered = df[df['dates'].dt.year == 2025]
```

### 10. **Timezones Handle Karna**
Datetime ko different timezones mein convert kar sakte hain using `.dt.tz_convert()`:
```python
# Convert to a specific timezone
df['dates'] = df['dates'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
```

### 11. **Timedelta Ka Use**
`Timedelta` objects ko create karke aap datetime ke saath duration-related operations perform kar sakte hain:
```python
# Subtract a timedelta from datetime
df['dates_minus_timedelta'] = df['dates'] - pd.Timedelta(days=1)
```

Yeh operations aapko pandas mein datetime data ko manipulate aur analyze karne mein kaafi madadgar hote hain.

This cheat sheet covers all essential features of the `datetime` library. Let me know if you need deeper examples or explanations!

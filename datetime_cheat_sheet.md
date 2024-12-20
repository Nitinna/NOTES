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

This cheat sheet covers all essential features of the `datetime` library. Let me know if you need deeper examples or explanations!

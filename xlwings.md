Here’s an **XLWings Cheat Sheet** to help you quickly get started and reference key commands for automating Excel with Python:

---

### **Setup**
- Install XLWings:
  ```bash
  pip install xlwings
  ```

- Import the library:
  ```python
  import xlwings as xw
  ```

---

### **Workbook and App Management**

1. **Create a new workbook:**
   ```python
   app = xw.App(visible=True)  # Starts Excel
   wb = xw.Book()             # Creates a new workbook
   ```

2. **Open an existing workbook:**
   ```python
   wb = xw.Book("file_path.xlsx")
   ```

3. **Save workbook:**
   ```python
   wb.save("file_path.xlsx")  # Save as
   wb.save()                  # Save current file
   ```

4. **Close workbook:**
   ```python
   wb.close()
   ```

5. **Quit Excel app:**
   ```python
   app.quit()
   ```

---

### **Sheets**

1. **Access a sheet by name or index:**
   ```python
   sheet = wb.sheets["Sheet1"]
   sheet = wb.sheets[0]
   ```

2. **Create a new sheet:**
   ```python
   wb.sheets.add(name="NewSheet")
   ```

3. **Delete a sheet:**
   ```python
   wb.sheets["SheetName"].delete()
   ```

---

### **Cells and Ranges**

1. **Read data from a cell:**
   ```python
   value = sheet.range("A1").value
   ```

2. **Write data to a cell:**
   ```python
   sheet.range("A1").value = "Hello, World!"
   ```

3. **Read/write ranges:**
   ```python
   # Read a range
   data = sheet.range("A1:C3").value

   # Write a list/2D array to a range
   sheet.range("A1").value = [[1, 2, 3], [4, 5, 6]]
   ```

4. **Auto-fit columns/rows:**
   ```python
   sheet.range("A1:C3").columns.autofit()
   sheet.range("A1:A10").rows.autofit()
   ```

5. **Clear content or formatting:**
   ```python
   sheet.range("A1:C3").clear_contents()  # Clear values
   sheet.range("A1:C3").clear()           # Clear everything
   ```

---

### **Formulas**

1. **Set a formula:**
   ```python
   sheet.range("B1").formula = "=SUM(A1:A10)"
   ```

2. **Get the formula:**
   ```python
   formula = sheet.range("B1").formula
   ```

---

### **Formatting**

1. **Change font size and color:**
   ```python
   rng = sheet.range("A1")
   rng.font.size = 12
   rng.font.color = (255, 0, 0)  # RGB for red
   ```

2. **Change cell background color:**
   ```python
   rng.color = (0, 255, 0)  # RGB for green
   ```

3. **Bold/italicize text:**
   ```python
   rng.font.bold = True
   rng.font.italic = True
   ```

---

### **Tables**

1. **Convert range to a table:**
   ```python
   table = sheet.tables.add(source=sheet.range("A1:C10"), name="MyTable")
   ```

2. **Access a table:**
   ```python
   table = sheet.tables["MyTable"]
   ```

3. **Remove a table:**
   ```python
   table.delete()
   ```

---

### **Charts**

1. **Create a chart:**
   ```python
   chart = sheet.charts.add()
   chart.chart_type = "line"
   chart.set_source_data(sheet.range("A1:B10"))
   ```

2. **Set chart title:**
   ```python
   chart.api[1].ChartTitle.Text = "My Chart"
   ```

---

### **Other Useful Tips**

1. **Access clipboard:**
   ```python
   xw.apps.active.api.CutCopyMode = False  # Clear clipboard
   ```

2. **Run Excel macros:**
   ```python
   wb.macro("MacroName")()
   ```

3. **Iterate over sheets:**
   ```python
   for sheet in wb.sheets:
       print(sheet.name)
   ```

4. **Screen updating (for better performance):**
   ```python
   app.screen_updating = False
   ```

---

Feel free to ask for more specific examples or further guidance!

## **openpyxl**
---
### **create a workbook**
---
~~~python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
# This is set to 0 by default. Unless you modify its value, you will always get the first worksheet by using this method.
~~~
~~~python
wb = Workbook()
ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
ws3 = wb.create_sheet("Mysheet", -1) # insert at the penultimate position
~~~
~~~python
ws.title = "New Title"
ws.sheet_properties.tabColor = "1072BA" # RRGGBB color code for the background color of the tab holding this title
~~~
~~~python
# Once you gave a worksheet a name, you can get it as a key of the workbook
ws3 = wb["New Title"]
# You can review the names of all worksheets of the workbook with the Workbook.sheetname attribute
print(wb.sheetnames)
# >>> ['Sheet2', 'New Title', 'Sheet1']
~~~
### **Playing with data**
~~~python
# Now we know how to get a worksheet, we can start modifying cells content. Cells can be accessed directly as keys of the worksheet:
c = ws['A4']
# This will return the cell at A4, or create one if it does not exist yet. Values can be directly assigned:
ws['A4'] = 4
# There is also the Worksheet.cell() method. This provides access to cells using row and column notation:
d = ws.cell(row=4, column=2, value=10)
~~~
~~~python
# Ranges of cells can be accessed using slicing:
cell_range = ws['A1':'C2']
# Ranges of rows or columns can be obtained similarly:
colC = ws['C']
col_range = ws['C:D']
row10 = ws[10]
row_range = ws[5:10]
~~~
~~~python
# You can also use the Worksheet.iter_rows() method:
[in]
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
  for cell in row:
      print(cell)
[out]
<Cell Sheet1.A1>
<Cell Sheet1.B1>
<Cell Sheet1.C1>
<Cell Sheet1.A2>
<Cell Sheet1.B2>
<Cell Sheet1.C2>
~~~
~~~python
# Likewise the Worksheet.iter_cols() method will return columns:
[in]
for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
  for cell in col:
      print(cell)
[out]
<Cell Sheet1.A1>
<Cell Sheet1.A2>
<Cell Sheet1.B1>
<Cell Sheet1.B2>
<Cell Sheet1.C1>
<Cell Sheet1.C2>
~~~
~~~python
# If you need to iterate through all the rows or columns of a file, you can instead use the Worksheet.rows property:
[in]
ws = wb.active
ws['C9'] = 'hello world'
tuple(ws.rows)
[out]
((<Cell Sheet.A1>, <Cell Sheet.B1>, <Cell Sheet.C1>),
(<Cell Sheet.A2>, <Cell Sheet.B2>, <Cell Sheet.C2>),
(<Cell Sheet.A3>, <Cell Sheet.B3>, <Cell Sheet.C3>),
(<Cell Sheet.A4>, <Cell Sheet.B4>, <Cell Sheet.C4>),
(<Cell Sheet.A5>, <Cell Sheet.B5>, <Cell Sheet.C5>),
(<Cell Sheet.A6>, <Cell Sheet.B6>, <Cell Sheet.C6>),
(<Cell Sheet.A7>, <Cell Sheet.B7>, <Cell Sheet.C7>),
(<Cell Sheet.A8>, <Cell Sheet.B8>, <Cell Sheet.C8>),
(<Cell Sheet.A9>, <Cell Sheet.B9>, <Cell Sheet.C9>))
~~~
~~~python
# or the Worksheet.columns property:
[in]
tuple(ws.columns)
[out]
((<Cell Sheet.A1>,
<Cell Sheet.A2>,
<Cell Sheet.A3>,
<Cell Sheet.A4>,
<Cell Sheet.A5>,
<Cell Sheet.A6>,
...
~~~
~~~python
# Both Worksheet.iter_rows() and Worksheet.iter_cols() can take the values_only parameter to return just the cell’s value:
[in]
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
  print(row)
[out]
(None, None, None)
(None, None, None)
~~~
### **Data storage**
~~~python
# Once we have a Cell, we can assign it a value:
[in]
c = ws['A4']
c.value = 'hello, world'
print(c.value)

[out]
'hello, world'
-------------------------------------------------
[in]
d = ws.cell(row=4, column=2, value=10)
d.value = 3.14
print(d.value)

[out]
3.14
-------------------------------------------------
#(note) Because of this feature, scrolling through cells instead of accessing them directly will create them all in memory, even if you don’t assign them a value
for x in range(1,101):
      for y in range(1,101):
          ws.cell(row=x, column=y)
#  -> This code dosen't create any cell value
-------------------------------------------------
# simple usage
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()
dest_filename = 'empty_book.xlsx'
ws1 = wb.active
ws1.title = "range names"
for row in range(1, 40):
     ws1.append(range(600))
ws2 = wb.create_sheet(title="Pi")
ws2['F5'] = 3.14
ws3 = wb.create_sheet(title="Data")
for row in range(10, 20):
    for col in range(27, 54):
        _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
wb.save(filename = dest_filename)
~~~


### **Saving to a file**
~~~python
# The simplest and safest way to save a workbook is by using the Workbook.save() method of the Workbook object:
wb = Workbook()
wb.save('balances.xlsx')
~~~

### **Loading from a file**
---
~~~python
[in]
from openpyxl import load_workbook
wb2 = load_workbook('test.xlsx')
print(wb2.sheetnames)

[out]
['Sheet2', 'New Title', 'Sheet1']
~~~

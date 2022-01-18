import gspread
import re

gc = gspread.service_account('secret.json')  # secret.json from Google Cloud Platform Account

spreadsheet = gc.open('private_demo')

# Get a worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0)

# Get a worksheet by name
worksheet1 = spreadsheet.worksheet('2022')

data = worksheet1.get_all_records()
print(data)

# Get a row or rows
row = worksheet1.get_values('A5:E5')  # row 5
rows = worksheet1.get_values('A5:F7')  # rows 5-7
print(row)
print(rows)

# Get a row by index
rows = worksheet1.row_values(3)
print(rows)

# Get a column by index
column = worksheet1.col_values(2)[1:]  # second column without Header of column
print(column)

# Get cell
cell_1 = worksheet1.get_values('D5')[0][0]
print(cell_1)

# Get cell using acell
cell_2 = worksheet1.acell('D5').value
print(cell_2)

# Search for cell
cell_3 = worksheet1.find('-10')
print(cell_3.row, cell_3.col)

# Search for many cells with value
cells = worksheet1.findall('-9')
print(cells)

# Search for partial matches with regular expression
reg = re.compile(r'99')
cells = worksheet1.findall(reg)

for cell in cells:
    print(cell.row, cell.col)

import gspread

gc = gspread.service_account('secret.json')  # secret.json from Google Cloud Platform Account
spreadsheet = gc.open('private_demo')
worksheet1 = spreadsheet.worksheet('2022')

# Update a cell
worksheet1.update('E5', -39)

# Update a cell based on row-column
worksheet1.update_cell(5, 5, -49)

existing_column = worksheet1.get_values('E2:E25')
new_column = [[round((float(i[0]) * 9 / 5 + 32), 1)] for i in existing_column]

worksheet1.update('G1:G25', [['Fahrenheit']] + new_column)

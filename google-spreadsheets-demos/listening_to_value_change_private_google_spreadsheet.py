import gspread
import time

# Establish Connection
gc = gspread.service_account('secret.json')  # secret.json from Google Cloud Platform Account

# Get spreadsheet
spreadsheet = gc.open('private_demo')

# Get worksheet
worksheet1 = spreadsheet.worksheet('2022')
worksheet2 = spreadsheet.worksheet('Watch')

while True:
    value1 = worksheet1.acell('G26').value
    time.sleep(2)
    value2 = worksheet2.acell('G26').value
    if value1 != value2:
        worksheet2.update('A1', 'CHANGED')

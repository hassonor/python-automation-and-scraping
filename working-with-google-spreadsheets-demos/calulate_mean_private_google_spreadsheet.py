import gspread
import statistics

# Establish Connection
gc = gspread.service_account('secret.json')  # secret.json from Google Cloud Platform Account

# Get spreadsheet
spreadsheet = gc.open('private_demo')

# Get worksheet
worksheet1 = spreadsheet.worksheet('2022')

# Get existing column
existing_column = worksheet1.get_values('G2:G25')

# Flatten the existing column
existing_column = [float(i[0]) for i in existing_column]

# Calculate average and add to Worksheet
average = statistics.mean(existing_column)
worksheet1.update('G26', average)

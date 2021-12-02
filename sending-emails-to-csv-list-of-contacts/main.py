import yagmail
from decouple import config
import pandas

PASSWORD = config('PASSWORD')

sender = "orhmeta@gmail.com"

yag = yagmail.SMTP(user=sender, password=PASSWORD)

df = pandas.read_csv('contacts.csv')
print(df)

for index, row in df.iterrows():
    subject = f"Thank you for applying to {row['role']}"
    contents = f'''
        Hey {row['firstName']} {row['lastName']}. 
        Welcome to our family. 
        Your new role will be: {row['role']}. 
        Good Luck!
    '''
    yag = yagmail.SMTP(user=sender, password=PASSWORD)
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent :-)")

import yagmail
from decouple import config
import time

sender = "orhmeta@gmail.com"
receiver = "sparklingltd@outlook.com"

subject = "This is Automate Email Sending :-)"

contents = """
    Hey this is the content of the Automated Mail ...
    Enjoy!
"""
PASSWORD = config('PASSWORD')
count = 0
while count < 1000:
    count += 1
    yag = yagmail.SMTP(user=sender, password=PASSWORD)
    yag.send(to=receiver, subject=f"{subject}-{count}", contents=contents)
    print("Email Sent :-) Num: " + str(count))

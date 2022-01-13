import yagmail
from decouple import config

sender = "orhmeta@gmail.com"
receiver = "hassonor@gmail.com"

subject = "This is Automate Email Sending :-)"

contents = """
    Hey this is the content of the Automated Mail ...
    Enjoy!
"""
PASSWORD = config('PASSWORD')
yag = yagmail.SMTP(user=sender, password=PASSWORD)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent :-)")

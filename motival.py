import smtplib
import datetime as dt
import random

#The config file with credentials
import config

EMAIL_FROM = 'alfredbootcamp@gmail.com'
PASSWORD = config.PASSWORD
EMAIL_TO = 'batmanbootcamp@yahoo.com'
MSG = 'Hey batman, whats for dinner?'
DATE_OF_BIRTH = dt.datetime(year= 1915, month= 4, day= 7)

# ---SEND-EMAIL---#

now = dt.datetime.now()
day = now.weekday()

if day >= 1 and day <= 5:

    #---GET-QUOTE---#

    with open('quotes.txt', 'r') as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes).strip()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_FROM, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_FROM, 
            to_addrs=EMAIL_TO, 
            msg=quote
            )
else:
    print("it's not a day to send a motival msg")

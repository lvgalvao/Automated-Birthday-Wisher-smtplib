import smtplib
import datetime as dt
import pandas as pd

#The config file with credentials
import config

EMAIL_FROM = 'alfredbootcamp@gmail.com'
PASSWORD = config.PASSWORD
MSG = 'Hey batman, whats for dinner?'
DATE_OF_BIRTH = dt.datetime(year= 1915, month= 4, day= 7)

#Load .csv file

df = pd.read_csv('src/birthdays.csv')
print(df(1))

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=EMAIL_FROM, password=PASSWORD)
#     connection.sendmail(
#         from_addr=EMAIL_FROM, 
#         to_addrs=EMAIL_TO, 
#         msg=MSG
#         )

# now = dt.datetime.now()
# year = now.year
# print(year)
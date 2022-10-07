import smtplib
import datetime as dt
import pandas as pd
from tkinter import *

import config


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv


#--UI--


BACKGROUND_COLOR = config.BACKGROUND_COLOR

root = Tk()
root.title("Automated Birthday Wisher")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def newBrithday():
    x1 = name.get()
    return print(x1)

canvas = Canvas(width=300, height=400)
canvas.pack()
# 1.1 Update name in birthdays.csv
name = Entry(root)
canvas.create_window(150,100, window=name)

# 1.2 Update email in birthdays.csv
# 1.3 Update year in birthdays.csv
# 1.4 Update month in birthdays.csv
# 1.5 Update day in birthdays.csv
# 1.6 Button save birthdays.csv
save = Button(text='Save new birthday', command=newBrithday)
canvas.create_window(150, 300, window=save)

df = pd.read_csv('src/birthdays.csv')
print(df)

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

root.mainloop()
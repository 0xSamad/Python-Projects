import datetime as dt 
import pandas as pd 
import smtplib
import random


# Replace `MY_EMAIL` and `MY_PASS` with your own pass

MY_EMAIL = "abdulsamadorakzai57@gmail.com" 
MY_PASS = "kxgfhzibntgltoqt" # not my pass (:


today_date = dt.datetime.now().day
today_month = dt.datetime.now().month

today = (today_month,today_date)

data = pd.read_csv("birthdays.csv")

birthdays_dictionary = { 
    (data_row['month'],data_row['day']): data_row for (index,data_row) in data.iterrows()
}

if today in birthdays_dictionary:
    birth_day_person = birthdays_dictionary[today]

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",birth_day_person['name'])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birth_day_person['email'],msg=f"Subject:Happy Birthday \n\n {contents}")
        print("mail sent")

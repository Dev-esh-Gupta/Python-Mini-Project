##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib
PLACEHOLDER = "[NAME]"

data = pandas.read_csv("birthdays.csv")
all_birthdays = data.to_dict("records")
print(all_birthdays)

today = dt.datetime.now()
day = today.day
month = today.month

for birthday in all_birthdays:
    if birthday['month'] == month and birthday['day'] == day:
        rand_choice = random.randint(1,3);
        with open(f"./letter_templates/letter_{rand_choice}.txt") as letter_file:
            name = birthday['name']
            letter_content = letter_file.read()
            birthday_letter = letter_content.replace(PLACEHOLDER,name)

        my_email = "deveshgupta110798@gmail.com"
        password = "nolr oxoo rnmg rlhp"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday['email'],
                                msg=f"Subject:Happy Birthday {birthday["name"]}"
                                    f"\n\n{birthday_letter}")




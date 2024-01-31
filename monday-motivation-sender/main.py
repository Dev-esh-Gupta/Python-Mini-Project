import random
import datetime as dt
import smtplib


# ----------- Holding of quote

with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines();
    wednesday_quote = random.choice(quotes_list)

time = dt.datetime.now()
print(time.weekday())
if time.weekday() == 2:
    my_email = "deveshgupta110798@gmail.com"
    password = "nolr oxoo rnmg rlhp"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="deveshgupta110798@yahoo.com",
                            msg=f"Subject:Stay Motivated!\n\n"
                                f"{wednesday_quote}")
from __future__ import unicode_literals
import cyprus_covid19 as covid
import time
from datetime import datetime
from tweet import tweet_new_cases

def tweet_and_print():
    print ("Running....")
    tweet_new_cases(date)
    print("Done!")

first_run = True
date = datetime.today().strftime("%d/%m/%Y")
print("Got the date")



while True:

    if first_run:
        print("Waiting for new cases..")
        yesterdays_total = covid.get_covid_cases("total")
        first_run = False

    current_total = covid.get_covid_cases("total")

    if current_total != yesterdays_total:

        tweet_and_print()
        first_run = True
        time.sleep(5)
        break

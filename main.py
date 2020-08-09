import cyprus_covid19 as covid
import time
from datetime import datetime
from tweet import tweet_new_cases

def tweet_and_print():
    print ("Running....")
    tweet_new_cases(date)
    print("Done!")

first_run = True

while True:

    while True:

        time_ = time.ctime()
        if "18:00:00" in time_ or "18:00:02" in time_ or "18:00:03" in time_ :
            date = datetime.today().strftime("%d/%m/%Y")
            print("Got the date")
            break

    while True:
        time_ = time.ctime()


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

        elif("06:00:00" in time_ or "06:00:02" in time_ or "06:00:03" in time_
             and current_total == yesterdays_total) :

            tweet_and_print()
            first_run = True
            time.sleep(5)
            break

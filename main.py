import tweepy as tw
import cyprus_covid19 as covid
import time
from datetime import datetime
from selenium import webdriver
import os

api_key = "Mz4BfkixaTnYgn2ULmT92ZIo1"
api_secret_key = "EKanjKerxoaMyFSCKomu7PgtKwwrh8r4w8xvbzYu5qn1Ubvh6l"
access_token = "1286222502923042818-mlVmmJ6rLhiLSsdeKobbxvDCVEySbs"
secret_access_token = "dmkBry6Crs3Fm1o9IYhpaJRNIvnIhgcFnPnihSHfNwgMl"
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api = tw.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

first_run = True

while True:

    time_ = time.ctime()

    #loop until its 23:00
    if first_run:
        print("Waiting..")
        first_run = False


    if "23:00:00" in time_ or "23:00:02" in time_ or  "23:00:03" in time_:

        print ("Running....")

        #assign vars
        todays_total = covid.get_covid_cases("total")
        new = covid.get_covid_cases("new")
        deaths = covid.get_covid_cases("deaths")
        tests = covid.get_covid_cases("tests")
        date = datetime.today().strftime("%d/%m/%Y")

        #change the announcement

        if new == "0":
            new_announcement = "\n\nΣήμερα δεν βρέθηκαν κρούσματα κορωνοϊού"
        else:
            new_announcement = "\n\nΣήμερα βρέθηκαν " + new + " κρούσματα"
        if deaths == "0":
            deaths_announcement = "Δεν υπήρξαν θάνατοι απο τον κορωνοϊό."
        else:
            deaths_announcement = "Σημερινοί θανάτοι: " + deaths
        if tests == "0":
            tests_announcement = "."
        elif tests != "0" and new != "0":
            tests_announcement = " απο " + tests + " εξετάσεις κορωνοϊού."
        elif tests != "0" and new == "0":
            tests_announcement = " και έγιναν " + tests + " εξετάσεις."


        #save twitter status in txt file (in order to use line breaks)
        file = open("status.txt", "w", encoding= "utf-8")
        file.write( date
                    + new_announcement + tests_announcement
                    + "\n" + deaths_announcement
                    + "\nΣύνολο: " + todays_total + " κρούσματα."
                    + "\n\nSources:\nhttps://corona.help"
                    + "\n\nΠροσοχή: Υπάρχει περίπτωση οι πληροφορίες να είναι λανθασμένες."
                    + "\n\n\n\u0023covid19cy \u0023covidcyprus \u0023menoumespiti")

        file.close()

        #read the file and update status
        file = open("status.txt", "r", encoding= "utf-8")
        api.update_status(status = file.read())

        first_run = True
        time.sleep(5)
        print("Done!")

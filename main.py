import tweepy as tw
import cyprus_covid19 as covid
import time
from selenium import webdriver
import os

auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api = tw.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

first_run = True

while True:

    #loop until its 23:00
    if first_run:
        print("Waiting..")
        yesterdays_total = "".join([x for x in list(covid.get_covid_cases("total")) if x != ","])
        first_run = False

    time_ = time.ctime()

    if "23:00:00" in time_ or "23:00:02" in time_ or  "23:00:03" in time_:

        print ("Running....")

        #assign vars
        todays_total = "".join([x for x in list(covid.get_covid_cases("total")) if x != ","])
        new = str(int(todays_total) - int(yesterdays_total))
        deaths = covid.get_covid_cases("deaths")
        tests = covid.get_covid_cases("tests")

        #change the announcement
        if deaths == "0":
            deaths_announcement = "Δεν υπήρξαν θάνατοι απο τον κορωνοϊό."
        else:
            deaths_announcement = "Σημερινοί θανάτοι: " + deaths

        if tests == "0":
            tests_announcement = "."
        else:
            tests_announcement = " απο " + tests + " εξετάσεις κορωνοϊού."

        #save twitter status in txt file (in order to use line breaks)
        file = open("status.txt", "w", encoding= "utf-8")
        file.write(("Σήμερα βρέθηκαν " + new + " κρούσματα" + tests_announcement
                    + "\n\n\n" + deaths_announcement
                    + "\nΣύνολο: "+ str(todays_total) + " κρούσματα."
                    + "\n\nSources:\nhttps://corona.help\nhttps://en.wikipedia.org/wiki/COVID-19_pandemic_in_Cyprus"
                    + "\nΠροσοχή: Υπάρχει περίπτωση οι πληροφορίες να είναι λανθασμένες."
                    + "\n\n\n\u0023covid19 \u0023covidcyprus \u0023menoumespiti"))

        file.close()

        #read the file and update status
        file = open("status.txt", "r")
        api.update_status(status = file.read())

        first_run = True
        time.sleep(5)
        print("Done!")

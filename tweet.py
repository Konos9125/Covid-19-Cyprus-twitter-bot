# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import cyprus_covid19 as covid
import tweepy as tw

api_key = "Mz4BfkixaTnYgn2ULmT92ZIo1"
api_secret_key = "EKanjKerxoaMyFSCKomu7PgtKwwrh8r4w8xvbzYu5qn1Ubvh6l"
access_token = "1286222502923042818-mlVmmJ6rLhiLSsdeKobbxvDCVEySbs"
secret_access_token = "dmkBry6Crs3Fm1o9IYhpaJRNIvnIhgcFnPnihSHfNwgMl"
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api = tw.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

def tweet_new_cases(date):
    #assign vars
    todays_total = covid.get_covid_cases("total")
    new = covid.get_covid_cases("new")
    deaths = covid.get_covid_cases("deaths")
    tests = covid.get_covid_cases("tests")

    #change the announcement

    if new == "0":
        new_announcement = u"\n\nΔεν βρέθηκαν κρούσματα κορωνοϊού"
    else:
        new_announcement = u"\n\nΒρέθηκαν " + new + " κρούσματα"
    if deaths == "0":
        deaths_announcement = u"Δεν υπήρξαν θάνατοι απο τον κορωνοϊό."
    else:
        deaths_announcement = u"Νέοι θανάτοι: " + deaths
    if tests == "0":
        tests_announcement = u"."
    else:
        tests_announcement = u" και έγιναν " + tests + " εξετάσεις."


    #save twitter status in txt file (in order to use line breaks)
    file = open("status.txt", "w")
    file.write( date
                + new_announcement + tests_announcement
                + "\n" + deaths_announcement
                + "\nΣύνολο: " + todays_total + " κρούσματα."
                + "\n\nSources:\nhttps://corona.help"
                + "\n\nΠροσοχή: Υπάρχει περίπτωση οι πληροφορίες να είναι λανθασμένες."
                + u"\n\n\n\u0023covid19cy \u0023covidcyprus \u0023menoumespiti")

    file.close()

    #read the file and update status
    file = open("status.txt", "r")
    api.update_status(status = file.read())

import tweepy as tw
import cyprus_covid19 as covid
import time
from selenium import webdriver
import os

auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

#assign stats to vars
corona_virus = covid.covid_stats()
total = corona_virus[0]
new = corona_virus[1]
tests = corona_virus[2]
deaths = corona_virus[3]

#change the announcement
if deaths == "0":
    deaths_announcement = "Δεν υπήρξαν θάνατοι απο τον κορωνοϊό."
else:
    deaths_announcement = "Σημερινοί θανάτοι: " + deaths

if tests == "0":
    tests_announcement = "."
else:
    tests_announcement = "απο " + tests + " εξετάσεις κορωνοϊού."

#set the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = options)
driver.set_window_position(-10000,0)


api = tw.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

wait = True

while True:

    #loop until its 20:30
    if wait:
        print("Waiting..")
        wait = False

    time_ = time.ctime()

    if "20:30:00" in time_:

        print ("Running....")

        #take a screenshot of the webpage with the covid graph and upload it on twitter
        driver.get('http://fullimg.atwebpages.com')
        time.sleep(5)
        driver.get_screenshot_as_file("screenshot.png")
        driver.quit()
        photo = api.media_upload("screenshot.png")

        #save twitter status in txt file (in order to use line breaks)
        file = open("status.txt", "w", encoding= "utf-8")
        file.write(("Σήμερα βρέθηκαν " + new + " κρούσματα" + tests_announcement
                    + "\n\n\n" + deaths_announcement
                    + "\nΣύνολο: "+ str(total) + " κρούσματα."
                    + "\n\nSources:\nhttps://corona.help\nhttps://en.wikipedia.org/wiki/COVID-19_pandemic_in_Cyprus"
                    + "\nΠροσοχή: Υπάρχει περίπτωση οι πληροφορίες να είναι λανθασμένες."
                    + "\n\n\n\u0023covid19 \u0023covidcyprus \u0023menoumespiti"))

        file.close()

        #read the file and update status
        file = open("status.txt", "r")
        api.update_status(status = file.read(), media_ids= [photo.media_id])

        wait = True
        print("Done!")

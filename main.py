import tweepy as tw
import cyprus_covid19 as covid
import time
from selenium import webdriver
import os


api_key = "Mz4BfkixaTnYgn2ULmT92ZIo1"
api_secret_key = "EKanjKerxoaMyFSCKomu7PgtKwwrh8r4w8xvbzYu5qn1Ubvh6l"
access_token = "1286222502923042818-mlVmmJ6rLhiLSsdeKobbxvDCVEySbs"
secret_access_token = "dmkBry6Crs3Fm1o9IYhpaJRNIvnIhgcFnPnihSHfNwgMl"
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)


corona_virus = covid.covid_stats()
total = corona_virus[0]
new = corona_virus[1]
tests = corona_virus[2]
deaths = corona_virus[3]

if deaths == 0:
    deaths_annouchment = "Σήμερα δεν υπήρξαν θάνατοι."
else:
    deaths_annouchment = "Σημερινοί θανάτοι: " + str(deaths)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = options)
driver.set_window_position(-10000,0)


api = tw.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


while True:
    
    time_ = time.ctime()

    if "19:00:00" in time_:

        print ("Please wait....")

        driver.get('https://covid19.ucy.ac.cy')
        time.sleep(30)
        driver.get_screenshot_as_file("screenshot.png")
        driver.quit()
        photo = api.media_upload("screenshot.png")


        file = open("status.txt", "w", encoding= "utf-8")
        file.write(("Σήμερα βρέθηκαν " + str(new) + " κρούσματα απο  " + str(tests) + " εξετάσεις κορωνοϊού."
                    + "\n\n\n" + deaths_annouchment
                    + "\nΣύνολο: "+ str(total) + " κρούσματα."
                    + "\n\nSources:\nhttps://corona.help\nhttps://covid19.ucy.ac.cy"
                    + "\n\n\n\u0023covid19 \u0023covidcyprus \u0023menoumespiti"))
        file.close()


        file = open("status.txt", "r")
        api.update_status(status = file.read(), media_ids= [photo.media_id])
        print("Done")

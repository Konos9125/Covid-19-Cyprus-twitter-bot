from bs4 import BeautifulSoup
import requests


def is_int(x):
    try:
        int(x)
        f = True
    except ValueError:
        f = False
    return f

def get_covid_cases(key):
    scrap = BeautifulSoup(requests.get("https://corona.help/country/cyprus").content, features="lxml")

    if key == "all":

        new_parent = list(scrap.find("div", attrs= {"class" : "col-xl-2 col-md-4 col-sm-6"}).text)

        new = "".join([x for x in new_parent if is_int(x)][4:])

        total = scrap.find("h2", attrs = {"class" : "text-bold-700 warning"}).text

        stats_parent = [x for x in list(scrap.find("div", attrs= {"class" : "row match-height"}).text) if x != "\n"]


        T_tests = max([index for index, item in enumerate(stats_parent) if item == "T"])
        s_tests = max([index for index, item in enumerate(stats_parent) if item == "s"])
        tests = "".join(stats_parent[s_tests + 1 : T_tests ])

        T_deaths = [index for index, item in enumerate(stats_parent) if item == "T"][3]
        s_deaths = [index for index, item in enumerate(stats_parent) if item == "s"][2]
        deaths = "".join(stats_parent[s_deaths + 1 : T_deaths])
        return total, new, tests, deaths
        
    elif key == "total":
    
        total = scrap.find("h2", attrs = {"class" : "text-bold-700 warning"}).text
        return total
        
    elif key == "new":
    
        new_parent = list(scrap.find("div", attrs= {"class" : "col-xl-2 col-md-4 col-sm-6"}).text)
        new = "".join([x for x in new_parent if is_int(x)][4:])
        
        return new
        
    elif key == "tests":
    
        stats_parent = [x for x in list(scrap.find("div", attrs= {"class" : "row match-height"}).text) if x != "\n"]
        
        T_tests = max([index for index, item in enumerate(stats_parent) if item == "T"])
        s_tests = max([index for index, item in enumerate(stats_parent) if item == "s"])
        tests = "".join(stats_parent[s_tests + 1 : T_tests ])
        
        return tests
        
    elif key == "deaths":
    
        stats_parent = [x for x in list(scrap.find("div", attrs= {"class" : "row match-height"}).text) if x != "\n"]
        
        T_deaths = [index for index, item in enumerate(stats_parent) if item == "T"][3]
        s_deaths = [index for index, item in enumerate(stats_parent) if item == "s"][2]
        deaths = "".join(stats_parent[s_deaths + 1 : T_deaths])
        return deaths
        
    else:
        new_parent = list(scrap.find("div", attrs= {"class" : "col-xl-2 col-md-4 col-sm-6"}).text)

        new = "".join([x for x in new_parent if is_int(x)][4:])

        total = scrap.find("h2", attrs = {"class" : "text-bold-700 warning"}).text

        stats_parent = [x for x in list(scrap.find("div", attrs= {"class" : "row match-height"}).text) if x != "\n"]


        T_tests = max([index for index, item in enumerate(stats_parent) if item == "T"])
        s_tests = max([index for index, item in enumerate(stats_parent) if item == "s"])
        tests = "".join(stats_parent[s_tests + 1 : T_tests ])

        T_deaths = [index for index, item in enumerate(stats_parent) if item == "T"][3]
        s_deaths = [index for index, item in enumerate(stats_parent) if item == "s"][2]
        deaths = "".join(stats_parent[s_deaths + 1 : T_deaths])
        
        return total, new, tests, deaths

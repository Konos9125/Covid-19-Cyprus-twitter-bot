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

    def get_all_stats():
        new_parent = list(scrap.find("div", attrs= {"class" : "col-xl-2 col-md-4 col-sm-6"}).text)

        new = "".join([x for x in new_parent if is_int(x)][5:])

        total = scrap.find("h2", attrs = {"class" : "text-bold-700 warning"}).text

        stats_parent = [x for x in list(scrap.find("div", attrs= {"class" : "row match-height"}).text) if x != "\n"]


        T_tests = max([index for index, item in enumerate(stats_parent) if item == "T"])
        s_tests = max([index for index, item in enumerate(stats_parent) if item == "s"])
        tests = "".join(stats_parent[s_tests + 1 : T_tests ])

        T_deaths = [index for index, item in enumerate(stats_parent) if item == "T"][3]
        s_deaths = [index for index, item in enumerate(stats_parent) if item == "s"][2]
        deaths = "".join(stats_parent[s_deaths + 1 : T_deaths])

        return total, new, tests, deaths

    if key == "all":
        return get_all_stats()

    elif key == "total":

        total = scrap.find("h2", attrs = {"class" : "text-bold-700 warning"}).text
        return total

    elif key == "new":

        new_parent = list(scrap.find("div", attrs= {"class" : "col-xl-2 col-md-4 col-sm-6"}).text)
        new = "".join([x for x in new_parent if is_int(x)][5:])

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
        return get_all_stats()

import bs4
import json
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options,executable_path="C:\\Users\\madhan\\Documents\\py automation\\geckodriver-v0.26.0-win64\\geckodriver.exe")
print("Getting started with browser....")
browser.get("https://www.justdial.com/Delhi/House-On-Rent/nct-10192844")
time.sleep(10)
browser.find_element_by_xpath("/html/body/section[16]/section/span").click()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(15)
html = browser.page_source
soup = bs4.BeautifulSoup(html, features="html.parser")
link = soup.find_all("li", {"class": "cntanr"})
major_list = []
print("Getting data...")
for i in link:
    d = {}
    name = i.find("span", {"class": "lng_cont_name"}).text
    ratings = i.find("span", {"class": "green-box"}).text
    ph_no = ""
    ph_lst = []
    for j in i.find_all("span", {"class": "mobilesv"}):
        ph_lst.append(j["class"])
    ph_lst = ph_lst[6:]
    for num in ph_lst:
        if num[1] == "icon-acb":
            ph_no += "0"
        elif num[1] == "icon-yz":
            ph_no += "1"
        elif num[1] == "icon-wx":
            ph_no += "2"
        elif num[1] == "icon-vu":
            ph_no += "3"
        elif num[1] == "icon-ts":
            ph_no += "4"
        elif num[1] == "icon-rq":
            ph_no += "5"
        elif num[1] == "icon-po":
            ph_no += "6"
        elif num[1] == "icon-nm":
            ph_no += "7"
        elif num[1] == "icon-lk":
            ph_no += "8"
        elif num[1] == "icon-ji":
            ph_no += "9"
    adrs = i.find("span", {"class": "cont_fl_addr"}).text
    d["name"] = name
    d["rating"] = ratings
    d["phone_no"] = ph_no
    d["address"] = adrs
    major_list.append(d)
print("Writing data..")
with open("sample.json", "wt") as outfile:
    for i in major_list:
        json_object = json.dumps(i, indent=4)
        outfile.write(json_object+"\n")

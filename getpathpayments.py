#!/usr/bin/env python
import csv
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import Request, urlopen, URLError, HTTPError
import re
from mechanize import Browser
import webcolors
import requests
import urllib 
from selenium import webdriver
from selenium.webdriver.common.by import By


with open("pathpayment.csv", "a+") as csvfile:
   csvwriter = csv.writer(csvfile,  delimiter=',')
   csvwriter.writerow(["Transaction","Amount","Fee","Time"])

driver = webdriver.Chrome()
driver.implicitly_wait(60)
with open("stellardata.csv") as f:
	#for i in range(18876):
	#for i in f:
	f.readline()
	reader = csv.reader(f, delimiter=",")
	for i in reader:
		if i[3] == "path_payment":
		   stellarurl = "https://steexp.com/tx/%s"%i[6]
		   driver.get(stellarurl)
		   time = driver.find_element(By.XPATH,"//table[@class='table']/tbody/tr[1]/td[2]").text
		   fee = driver.find_element(By.XPATH,"//table[@class='table']/tbody/tr[2]/td[2]").text
		   amount = driver.find_element(By.XPATH,"//table[@class='table-striped table-hover table-condensed table']/tbody/tr[1]/td[2]").text
		   with open("pathpayment.csv", "a+") as csvfile:
					csvwriter = csv.writer(csvfile,  delimiter=',')        
					csvwriter.writerow([i[6],amount,fee,time])          
		else:
			print i[3]
			continue
driver.quit()


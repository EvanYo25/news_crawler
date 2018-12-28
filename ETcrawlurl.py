import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
from string import digits
import json
from pprint import pprint
import sys
import gc
import time

year = (sys.argv[1])
month = (sys.argv[2])
# date = (sys.argv[3])
year2018 = [0,31,28,31,30,31,30,31,31,30,31,30,17]
date = year2018[int(month)]


# write file route
route = './et'+year+month+'url.txt'
fo = open(route,'w')
count = 0

for j in range(1,date+1):
	if j<10:
		j = '0'+str(j)
	else:
		j = str(j)

	homepage = "https://www.ettoday.net/news/news-list-"+year+"-"+month+"-"+j+"-0.htm"

	driver = webdriver.Chrome('/Users/evanyo25/Applications/Chrome Apps.localized/chromedriver')
	driver.get(homepage)
	print('start_scrolling')
	for i in range(100):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(0.5)
	print('end_scrolling')

	elem = driver.find_element_by_class_name('part_list_2')
	elem2 = elem.find_elements_by_xpath('//h3/a[@target="_blank"]')

	for i in elem2:
		s_url = i.get_attribute('href')
		if(('https://www.ettoday.net/news/'+year+month+j) in s_url):
			count += 1
			# print(s_url)
			# print(i.text)
			fo.write(s_url)
			fo.write('\n')
	print(j)
	print(count)
	driver.quit()

fo.close()

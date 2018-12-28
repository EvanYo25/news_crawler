import urllib.request
from bs4 import BeautifulSoup
from string import digits
import json
from pprint import pprint
import sys
import gc

month = int(sys.argv[1])
year2018 = [0,31,28,31,30,31,30,31,31,30,31,30,17]
date = year2018[month]

#
path_raw_data = './udn2018'+str(month)+'url.txt'
fo = open(path_raw_data,"w")

count = 0
for date in list(range(date)):
	dt = date+1
	m = str(month)
	d = str(dt)
	if(len(m)<2):
		m = '0'+m
	if(len(d)<2):
		d = '0'+d
	print(m+d)
	quote_page = "https://udn.com/news/archive/0/0/2018/"+ m +"/"+ d +"/"
	# quote_page = "https://udn.com/news/archive/0/0/2018/01/01/"
	page = urllib.request.urlopen(quote_page)
	soup = BeautifulSoup(page,'html.parser')
	day_total = soup.find('span', {'class':'total'})
	day_total = ''.join(c for c in day_total.string if c in digits)
	print(day_total)

	for k in range(1,int(day_total)):
		page = urllib.request.urlopen(quote_page+str(k))
		soup = BeautifulSoup(page,'html.parser')
		name_box = soup.find('div', attrs={'id': 'ranking_body'})
		pid = name_box.findAll('a')
		for i in pid:
			sm_url = "https://udn.com"+i.get('href')
			print(sm_url)
			fo.write(sm_url)
			fo.write('\n')
			count += 1
		print (count)
fo.close()

print(count)


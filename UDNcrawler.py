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
path_raw_data = './udn2018'+str(month)+'.json'
raw_data = {}
raw_data['src'] = 'udn'
data = []

count = 0
for date in list(range(date)):
	dt = date+1
	m = str(month)
	d = str(dt)
	if(len(m)<2):
		m = '0'+m
	if(len(d)<2):
		d = '0'+d
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
			sm_page = urllib.request.urlopen(sm_url)
			sm_soup = BeautifulSoup(sm_page,'html.parser')
			sm_title = sm_soup.find('h1',{'id':'story_art_title'})
			if(sm_title):
				print(sm_title.string)
				sm_keywds = sm_soup.find('div',{'id':'story_tags'})
				tmp = {}
				tmp['title'] = sm_title.string
				if(sm_keywds):
					tmp_tag = []
					sm_keywd = sm_keywds.findAll('a')
					for j in sm_keywd:
						print(j.string)
						tmp_tag.append(j.string)
					tmp['tags'] = tmp_tag
					data.append(tmp)
					pprint(data)
					count+=1
					if(count%10==0):
						print(count)
				else:
					print('no tags')
				del tmp
				gc.collect()
			else:
				print('no title')
			del sm_page, sm_soup, sm_title
			gc.collect()
	# 		if(count>10):
	# 			break
	# 	break
	# break
raw_data['data'] = data

with open(path_raw_data, 'w', encoding='utf-8') as f:
    json.dump(raw_data, f)

with open(path_raw_data, 'r', encoding='utf-8') as f:
    data = json.load(f)

pprint(data)
print(count)


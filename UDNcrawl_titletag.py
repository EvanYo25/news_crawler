import urllib.request
from bs4 import BeautifulSoup
from string import digits
import json
from pprint import pprint
import sys
import gc

filename = sys.argv[1]
index = int(sys.argv[2])
start = (index-1)*1000+1
end = start+1000


path_raw_data = './'+filename+'_'+str(index)+'.json'
raw_data = {}
raw_data['src'] = 'udn'
data = []

run = 1
with open(filename+'.txt') as fh:
	line = fh.readline()
	while line:
		if(run>end):
			break
		if(run>=start):
			print(line.strip())
			try:
				sm_page = urllib.request.urlopen(line)
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
						# pprint(data)
					else:
						print('no tags')
					del tmp
					gc.collect()
				else:
					print('no title')
				del sm_page, sm_soup, sm_title
				gc.collect()
				print(run)		
			except Exception as e:
				print("type error: " + str(e))

		line = fh.readline()
		run += 1


raw_data['data'] = data

with open(path_raw_data, 'w', encoding='utf-8') as f:
    json.dump(raw_data, f)

with open(path_raw_data, 'r', encoding='utf-8') as f:
    data = json.load(f)

pprint(data)
print(run)



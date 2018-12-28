import urllib.request
from bs4 import BeautifulSoup
from string import digits
import json
from pprint import pprint
import sys
import gc

filename = sys.argv[1]
index = int(sys.argv[2])
# artOrNot = int(sys.argv[3]) # 1 for yes , 0 for no
start = (index-1)*1000+1
end = start+1000


path_raw_data = './'+filename+'_'+str(index)+'.json'
raw_data = {}
data = [{'tags':[],'title':'none'} for x in range(1000)]

run = 1
datacount = 0
with open(filename+'.txt') as fh:
	line = fh.readline()
	while line:
		if(run>end):
			break
		if(run>=start):
			print(line.strip())
			try:
				sm_page = urllib.request.urlopen(line, timeout=5)
				sm_soup = BeautifulSoup(sm_page,'html.parser')
				sm_title = sm_soup.find('h1',{'class':'title'})
				sm_keywds = sm_soup.find('p',{'class':'tag'})
				if(sm_title and sm_keywds):
					print(sm_title.string)
					data[datacount]['title'] = sm_title.string
					sm_keywd = sm_keywds.findAll('a')
					for j in sm_keywd:
						print(j.string)
						data[datacount]['tags'].append(j.string)
						# pprint(data)
					datacount += 1
					del sm_keywd
					gc.collect()
				else:
					print('no title or tags')
				del sm_page, sm_soup, sm_title, sm_keywds
				gc.collect()
				print("reading news number:"+str(run))
				print("saving "+str(datacount)+" news")
			except Exception as e:
				print("type error: " + str(e))
		line = fh.readline()
		run += 1
print(len(data))
del data[datacount:1000]
print(len(data))

raw_data['src'] = 'udn'
raw_data['data'] = data

with open(path_raw_data, 'w', encoding='utf-8') as f:
    json.dump(raw_data, f)

with open(path_raw_data, 'r', encoding='utf-8') as f:
    data = json.load(f)

pprint(data)
print(run)



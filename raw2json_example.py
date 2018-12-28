import json
from pprint import pprint

path_raw_data = './udn2018.json'

raw_data = {'data': [{'title': "是否繼續當球員 郭泓志保留任何可能性",
                      'tags': ["郭泓志", "富邦悍將"]},
                      {'title': "王老吉涼水舖再爆欠薪 員工慘訴：沒錢吃飯",
                      'tags': ["王老吉", "欠薪"]}]}
with open(path_raw_data, 'w', encoding='utf-8') as f:
    json.dump(raw_data, f)

with open(path_raw_data, 'r', encoding='utf-8') as f:
    data = json.load(f)

pprint(data)
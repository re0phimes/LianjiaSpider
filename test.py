url = 'https://bj.lianjia.com/chengjiao/'

import requests
from pyquery import PyQuery as pq
r = requests.get(url)
doc = pq(r.text)
# links = doc('div.page-box.house-lst-page-box')
links2 = doc('div.contentBottom.clear')
for a in links2.items():
    print(a)


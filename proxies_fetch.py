# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from cfg import config
import random


def get_html(url, use_proxy=False, time_out=5):
    agent = random.choice(config.USER_AGENTS)
    header = {'User-Agent': agent}
    if use_proxy:
        r = requests.get(url, headers=header, timeout=time_out, proxies={'http': '114.55.6.45:37711'})
    else:
        r = requests.get(url, headers=header, timeout=time_out)
    return r.text

url_0 = 'http://www.xicidaili.com/nn'

url_1 = 'http://cn-proxy.com/'

url_2 = 'http://www.getproxy.jp/en/china/1'







content0 = get_html(url_0)

content1 = get_html(url_1, use_proxy=True)

content2 = get_html(url_2, use_proxy=True)





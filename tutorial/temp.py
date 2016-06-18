import grequests
import bs4
import requests
import pandas as pd


url = 'http://www.lagou.com'

url = 'http://www.xicidaili.com/nn'

proxyDict = {'http': '114.55.6.45:37711'}
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.125 Safari/537.36'}

r = requests.get(url, timeout=10, headers=header)

content = r.text

soup = bs4.BeautifulSoup(r.content, 'lxml')
pages = soup.select('div.pagination a')
tbody = soup.select('table')
print tbody


base_url = 'http://www.xicidaili.com'


def derive_table(tbody_soup):
    tbody_list = []
    trs = tbody_soup.select('tr')
    for tr in trs:
        rows = tr.select('td')
        list_rows = [row.text.strip() for row in rows]
        if list_rows:
            tbody_list.append(list_rows)
    df = pd.DataFrame(tbody_list)
    filter_col = (df == '').apply(lambda x: not all(x), axis=0)
    return df.ix[:, filter_col]

temp_df = derive_table(tbody[0])
temp_df.columns = ['ip', 'port', 'addr', 'hide', 'type', 'len', 'check_time']
temp_df['id'] = temp_df['ip'] + ':' + temp_df['port']
temp_df = temp_df[['id', 'ip', 'port', 'type', 'addr']]

from sqlalchemy import create_engine

engine = create_engine("mysql://root:dadaerer@localhost/proxy_ip?charset=utf8",
                       encoding='utf8', pool_recycle=3306)
conn = engine.connect()
conn.execute('show tables').fetchall()
temp_df['addr'] = temp_df['addr'].str.encode('utf8')
temp_df.to_sql('test', engine, flavor='mysql', index=False, if_exists='append')


ipp = conn.execute('select * from test').fetchall()
pd.DataFrame(ipp)
print len(ipp)

conn.close()
temp_dict = temp_df.to_dict()
df = pd.DataFrame(temp_dict)

ip_list = (temp_df[1] + ':' + temp_df[2]).tolist()

temp_df['proxy_ip'] = ip_list

for row in temp_df.iterrows():

    print row
baidu_url = 'http://202.108.22.5/'

# test_r = requests.get(baidu_url, timeout=5, proxies={'http': temp_df['proxy_ip'][2]})
# test_r = requests.get(baidu_url, timeout=5)
# test_r.content.find('11000002000001')

# soup = bs4.BeautifulSoup(test_r.content, 'lxml')


def timeout_handler(request, exception):
    return None

reqs = [grequests.get(baidu_url, proxies={'http': proxy_ip}, timeout=5) for proxy_ip in temp_df['id']]



greqs = grequests.map(reqs, exception_handler=timeout_handler)

verify_list = [rsp.content.find('11000002000001') if rsp else -2 for rsp in greqs]




sidebar = soup.select('div.sidebar dd a')


href = sidebar.attrs['href']
tj_id = sidebar.attrs['data-lg-tj-id']
tj_no = sidebar.attrs['data-lg-tj-no']


url = 'http://www.kuaidaili.com/free/'
s = requests.Session()
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.125 Safari/537.36'}
r = s.get(url, cookies={'form-my': 'browser'}, headers=header)
print r.content




import _mysql
db = _mysql.connect('localhost', 'root', 'dadaerer')

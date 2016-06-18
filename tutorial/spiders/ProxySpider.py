import scrapy
import bs4
from tutorial.items import ProxyItem
from util.utility import derive_table
import time


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['xicidaili']
    start_urls = [
        'http://www.xicidaili.com/nn'
    ]

    def start_requests(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.125 Safari/537.36'
        }
        yield scrapy.Request('http://www.xicidaili.com/nn', headers=header, callback=self.parse, dont_filter=True)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        pages_ = soup.select('div.pagination a')
        base_url = 'http://www.xicidaili.com'
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.125 Safari/537.36'
        }
        for href in pages_:
            url = base_url + href.attrs['href']
            print '\n\n\n\n'
            print url
            print '\n\n\n\n'
            yield scrapy.Request(url, dont_filter=True, headers=header, callback=self.parse_proxy_details)
            # time.sleep(1)

        # url = base_url + pages_[0].attrs['href']
        # yield scrapy.Request(url, dont_filter=True, headers=header, callback=self.parse_proxy_details)

    def parse_proxy_details(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        tbody = soup.select('table')[0]
        proxy_df = derive_table(tbody)
        proxy_df.columns = ['ip', 'port', 'addr', 'hide', 'type', 'len', 'check_time']
        proxy_df['id'] = proxy_df['ip'] + ':' + proxy_df['port']
        proxy_df = proxy_df[['id', 'ip', 'port', 'type', 'addr']]
        item = ProxyItem()
        item['ip_table'] = proxy_df.to_dict()
        yield item



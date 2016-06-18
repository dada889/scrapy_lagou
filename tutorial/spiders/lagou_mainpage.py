
import scrapy
import bs4

from tutorial.items import LagouMainItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = [
        'http://www.lagou.com'
    ]

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text)
        main_item = LagouMainItem()
        jobs = soup.select('div.sidebar dd a')

        for job_obj in jobs:
            main_item['job_href'] = job_obj.attrs['href']
            main_item['tj_id'] = job_obj.attrs['data-lg-tj-id']
            main_item['tj_no'] = job_obj.attrs['data-lg-tj-no']
            main_item['job_name'] = job_obj.text
            yield main_item




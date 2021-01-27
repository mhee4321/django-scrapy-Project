import scrapy
from newscrawling.items import NewscrawlingItem
from scrapy.http import Request

URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&page=%s'

start_page = 1

def remove_space(titles:list) -> list:
    result = []
    for i in range(len(titles)):
        if len(titles[i].strip()) > 0:
            result.append(titles[i].strip())
    return result

class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]
    
    def start_requests(self):
        for i in range(10):
            yield Request(url=URL % (i + start_page), callback=self.parse)


    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt[2]/a/text()').extract()
        converted_titles = remove_space(titles)
        contents = response.css('.lede::text').extract()
        companies = response.css('.writing::text').extract()
        saved_times = response.css('.is_new::text').extract()
        # links = response.xpath('.photo img').extract()


        items = []
        for idx in range(len(converted_titles)):
            item = NewscrawlingItem()
            item['title'] = converted_titles[idx]
            item['content'] = contents[idx]
            item['company'] = companies[idx]
            item['saved_time'] = saved_times[idx]
            items.append(item)

        return items
     

from scrapy.spiders import Spider
import re, urllib2
from scrapy.selector import HtmlXPathSelector
from BilibiliCrawler.items import BiliItem 
import csv

class DmozSpider(Spider):
    name = "bilibili"
    allowed_domains = ['bilibili.tv']
    start_urls = []

    def __init__(self, begin = None, end = None):
        csvfile = file('bilibili_avNo.csv', 'rb')
        reader = csv.reader(csvfile)
        for line in reader:
            self.start_urls.append('http://www.bilibili.tv/video/av' + str(line[0]))




    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        if hxs.select("//center").extract():
            return
        bili = BiliItem()

        bili['url']      = response.url        
        bili['avNo']     = int(re.search(r'\d+', str(response.url)).group())
        bili['title']    = hxs.xpath("//h1/text()").extract()[0]
        bili['time']     = hxs.xpath("//time/i/text()").extract()[0]
        bili['category'] = hxs.xpath('//a[@class="on"]/text()').extract()[0]
        bili['up']       = hxs.xpath('//a[@class="name"]/text()').extract()[0]

        if bili['title']:
            bili['comment'] = int(re.findall(re.compile(r"acount.{2}\d+"),urllib2.urlopen("http://api.bilibili.com/x/reply?jsonp=jsonp&type=1&sort=0&oid=" + str(bili['avNo'])).read())[0][8:])
            content = urllib2.urlopen("http://interface.bilibili.com/count?key=5cb9d3f30568fd06bb388d13&aid=" + re.search(r'\d+', str(response.url)).group()).read()
            bili['click']    = int(re.findall(re.compile(r"ji.{9}\d+"),content)[0][11:])
            bili['coin']  = int(re.findall(re.compile(r"es.{8}\d+") ,content)[0][10:])
            bili['sc'] = int(re.findall(re.compile(r"stow_count.{9}\d+"),content)[0][19:])
            bili['dm']   = int(re.findall(re.compile(r"dm_count.{8}\d+"),content)[0][16:])

        del content,hxs
        yield bili

    
    
    
    
    
    
    
    
    
    
    
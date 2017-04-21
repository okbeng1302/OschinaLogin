# -*- coding: utf-8 -*-
import scrapy
import logging

from scrapy.selector import Selector
class OchinaSpider(scrapy.Spider):
    name = "ochina"
    allowed_domains = ["www.oschina.net"]
    #start_urls = ['http://oschina.net/']
    headers = {
    	'Host':'www.oschina.net',
    	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    	'Accept':'application/json, text/javascript, */*; q=0.01',
    	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    	'Accept-Encoding':'gzip, deflate, br',
    	'Referer':'http://www.oschina.net',
    	#'Cookie':'bid=VfGaWhfWIF8; ps=y',
    	'Connection':'keep-alive',
    	#'Upgrade-Insecure-Requests':'1'
    }
    formdata2 = {
    	'email':'15120045@njtu.edu.cn',
    	'pwd':'70aeff85a2daa0cfecf4cc816ef7cdeb9124b898',
    	'verifyCode':'',
    	'save_login':'0'
    }
    def start_requests(self):

    	return [scrapy.Request(url='https://www.oschina.net',method='get',cookies={'_user_behavior_':'4761e11b-abaf-49a9-9132-24bf449a9f0f','oscid':'4PpfWJFgaYBL0rdop%2FHhmei3BNm2DDV1PeX2CQ8wzefpkCHC1LShVbEBQM%2BsLM0jwJTJpqrzKXECzrVkxTmRBlejF4Rg8S0qaQpLqzUHyaD19r4smcHzru33MS1PWtqx79QspDmM3RARDd71PWXvza%2FSGWadDdrD3QXcLhN3ruAoTcIjSO%2FSgg%3D%3D','Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b':'1492580323,1492666551,1492765230,1492765477','Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b':'1492777346'},headers=self.headers,callback=self.parse_one,dont_filter=True)]
    
    def parse_one(self,response):
    	sel = Selector(response)
    	title = sel.xpath('//title/text()').extract()[0]
    	count = 0
    	count = count + 1
    	links = sel.xpath('.//a/@href').extract()
    	for link in links:
    		# print link
    		if not link.startswith('https://'):
    			if not link.startswith('http://'):
    				link = 'https://www.oschina.net' + link
    		yield scrapy.Request(url=link,callback=self.parse_one,headers=self.headers)

    	print response.url + '3'
     	open('e:\hanhan\\'+ title + '.txt', 'w+').write(response.body)
     	# logging.log(logging.WARNING,response.body)
    	# return [scrapy.Request(url='https://www.oschina.net/home/login',headers=response.headers,meta={'cookiejar':2},callback=self.parse_login, dont_filter=True)]

    # def parse_login(self,response):
    # 	print response.headers
    # 	print 'Prepare logining.....' + response.url
    # 	return [scrapy.FormRequest.from_response(response,
    #                                             url='https://www.oschina.net/action/user/hash_login',
    # 											formdata=self.formdata2,
    # 											headers=response.headers,
    # 											meta=response.meta['cookiejar'],
    # 											callback=self.after_login,
    #                                             dont_filter=True
    # 											)]
    # def after_login(self,response):
    # 	print 'logined =====' + response.url
    # 	print response.status

    #     yield scrapy.FormRequest(url='https://www.oschina.net',meta={'cookiejar':response.meta['cookiejar']},
    #                     headers = self.headers,
    #                     callback = self.parse_item
    #                     )
    # def parse_item(self,response):
    #     print response.url + '3'
    # 	open('e:\hanhan\\ochina.txt', 'w+').write(response.body)
    # 	#logging.log(logging.WARNING,response.body)


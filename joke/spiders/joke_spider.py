import scrapy
from joke.items import JokeItem


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'}


class JokeSpider(scrapy.Spider):
    name = 'joke'

    def start_requests(self):
        urls = [
            'http://www.qiushibaike.com/text/page/1',
        ]
     #   start_urls = [
      #      'http://www.qiushibaike.com/text/page/',
      #  ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,headers=headers)

    def parse(self, response):
        item = JokeItem()
        #page = response.url.split("/")[-2]
      #  info=response.body
        #print(info)
     #   print(response)
        #print(type(info))
        for data in response.xpath('//div[@class="article block untagged mb15 typs_hot"]'):
            item['picture'] = data.xpath('./div[@class="author clearfix"]/a[1]/img/@src').extract_first()
            item['author'] = data.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
            item['age'] = data.xpath('./div[@class="author clearfix"]/div/text()').extract_first()
            item['sex'] = data.xpath('./div[@class="author clearfix"]/div/@class').extract_first()
            item['content']= data.xpath('./a/div/span/text()').extract_first()
           # item['content'] = data.xpath('./a/div[@class="content"]/span/descendant::text()').extract_first()
            item['vote'] = data.xpath('./div[2]/span/i/text()').extract_first()
            item['comment']= data.xpath('./div[2]/span[2]/a/i/text()').extract_first()
      #print(comment)
       #     print(vote)
        #    print(content)
         #   print(sex)
          #  print(age)
           # #print(picture)
            #print(author)
            yield item

   # print(author)
#    print('haha')
#    next_page = response.xpath('// *[ @ id = "content-left"] / ul / li[8] / a /@href').extract_first()
    #next_page='http://www.qiushibaike.com'+ next_page
 #   print(next_page)
  #  // *[ @ id = "content-left"] / ul / li[8] / a / span
  #  if next_page is not None:
   #     yield scrapy.Request(response.urljoin(next_page))
      #  next_page = response.urljoin(next_page)
     #   print(next_page)
      #  yield scrapy.Request(next_page, callback=self.parse,headers=headers)
   #     #yield scrapy.Request(next_page,headers=headers)
        #pass

       # next_page = self.start_urls[0] + next_page
       # yield Request(url=next_page, headers=headers, callback=self.parse)

     #       yield Request(self.host + next_page, callback=self.parse_start_url)
 #   filename = 'quotes-%s.html' % page
  #  with open(filename, 'wb') as f:
 #       f.write(response.body)
  #  self.log('Saved file %s' % filename)
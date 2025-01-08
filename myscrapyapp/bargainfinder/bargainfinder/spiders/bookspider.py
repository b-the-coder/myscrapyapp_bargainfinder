import scrapy
from bargainfinder.items import BookItem
from urllib.parse import urlencode 
from scrapy.http import Request



class EcommerceSpider(scrapy.Spider):
    name = "adidasspider"
    allowed_domains = ["www.adidas.com"]
    start_urls = ['https://www.adidas.com/us/women-hoodies_sweatshirts']

    def start_requests(self):
        cookies = {
            '_abck': 'A9CEEAE8E0A89A9DDE1B0A75834549F8~-1~YAAQRiTDF8cEXe6TAQAA5/sfQw2sia+QY5rJhgj8i3T8bY71gTLBPnltnZPluUNeDGDDvWdnhdt6dp+bRg6ZBc4AADjhkUkE0B6XlndmngCoMJJ4SL38BPIF0f3tEEDDO2LpsPNjRBkTGqi6XWglxf/8yeeEI8+liGX2x5rJREQfiUi6URDfePwdDoqTrjrLRPGVrcusi1ljzJTlRriuROT/wn4H4HS05f8+EiN9F0prIIaoaREN7rY5B1VN4s/Oh9e1ucnYAPCDC+jkJBOOmHbrl9MwmBcOwbZVk6UtzHlEGmsUeSXuUJhDKoGrP+MeCzMS1XV1cig84+SO6N+lNA==~-1~-1~-1',
            'bm_s': 'YAAQRiTDF8gEXe6TAQAA5/sfQwI7f/XLVZUYYnImcXr2cA+ogJlc+/8iiGVNSxfG+CvFkUzqXsl2twT+IErj8PEBe/FOZ/moAVSQ3yO2f0SsuwYfHw3ioyvakB9y3r13LlQ30FEQYJ0pBkQUQU5e34qwM+NGLBbOJyLnhpMVF0iJ8u/pRiavoR9b30SgQcRA2l+0AFSqcLuIrm5YyNfsnuzedoGABPg9c7p4zvhnpGjUATWxLinYuU4dd9dmZp09BduvqqJTy0QAMLeMIy/67YSkX7pElyo0z4qC3PI3at82+oAgOHjFPWhZ8d+QfoYs3rFGm37zE1cP3AuNfXO2DFX2m9zwlnM2',
            'bm_ss': 'e919a75364',
            'bm_sz': 'CC119946873B0C8757A0EFF86136EAEC~YAAQEhMoF1atG7mTAQAAkXDWQhos4ckBC220tsYCd1I164rEgdxPvQ96HM57gSfJcF3pn0XH790KSLEa0NL/0W43Dwj8k8F6T0Gb8Pe4AeFxYYx3XMtNvtsyEbjIwqZYuH65dVGruy4WrmHMo9ltpiie7Qyu44xMtRg3vnx1xUJzpqvaji70vKfwMvheoKKtzAxuZuf5DMxsds15iGaRgb9qq5zJUHiwZ3vlgOAKbCOnvylHutY+uj2C4cUJ13dYXykPQT0BC5pRuUc6IE+sXM2QAhGIeQafNJD3TKjHiJlMaSVihpReY5uSvCn+nZ4WDoSjGGhEGyPKU2W6RTkhHSZ73dzCWO2fT4WD1m7Hr+FREgc6I/W8jET1528kU+PcFuPC9hTE+EGckvVHa0Yqws02bEyJqMzDYtrLkcyBtZIkg8N2IXdvTo31WruZY4HUo0BVh4WUoxdspQq9Q/eWwmEI8Bs6RgbKJKOGj59QM4yyVLV8ia5Kse/13NgsKEHUSNeOqTIOFDYOklJeo+2l+LtwyQ==~3227971~3359285',
            'adidas_country': 'us',
            'akacd_phased_PLP': '3913743791~rv=61~id=a5c12438fe81e88fb3f1f1552fe2af2d',
            'geo_country': 'US',
            'geo_ip': '96.242.188.127',
            'geo_state': 'NJ',
            'onesite_country': 'US'
        }

        for url in self.start_urls:
            yield Request(url, cookies=cookies, callback=self.parse)


    def parse(self, response):
        
        hoodies = response.css('div.product-card_product-card-content___bjeq')
        print(hoodies)
        # Iterate through each hoodie
        for hoodie in hoodies:
        # Extract product name
            product_name = hoodie.css('p[data-testid="product-card-title"]::text').get()

        # Extract price
            price = hoodie.css('div[data-testid="primary-price"]::text').get()

        # Extract number of colors
            colors_text = hoodie.css('p[data-testid="product-card-colours"]::text').get()
            num_colors = int(colors_text.split()[0]) if colors_text else 0

        # Check if the product is new
            is_new = 'new' in hoodie.css('div.product-card-description_badge__m75SV::text').get('').lower()


        # Yield the extracted information
            yield {
                'product_name': product_name,
                'price': price,
                'num_colors': num_colors,
                'is_new':is_new
            }
        
        
        # yield {

        #     'url' : response.url,
        #     'title':  response.css('.product_main h1::text').get(),
        #     'product_type': table_rows[1].css("td ::text").get(),
        #     'price_excl_tax' : table_rows[2].css("td ::text").get(),
        #     'price_incl_tax': table_rows[3].css("td ::text").get(),
        #     'tax': table_rows[4].css("td ::text").get(),
        #     'availability':table_rows[5].css("td ::text").get(),
        #     'num_reviews':table_rows[6].css("td ::text").get(),
        #     'stars': response.css("p.star-rating").attrib["class"],
        #     'category':response.xpath("//ul[@class = 'breadcrumb']/li[@class = 'active']/preceding-sibling::li[1]/a/text()").get(),
        #     'description':response.xpath("//div[@id= 'product_description']/following-sibling::p/text()").get(),
        #     'price': response.css('p.price_color ::text').get(),

        # }

   #      for book in books:
   #          relative_url = book.css('h3 a ::attr(href)').get()
   #          if'catalogue/' in relative_url:
   #             book_url = 'https://books.toscrape.com/' + relative_url
   #          else:
   #             book_url = 'https://books.toscrape.com/catalogue/' + relative_url
   #          yield scrapy.Request(url= book_url, callback = self.parse_book_page)
 
            
   #      next_page = response.css('li.next a ::attr(href)').get()

   #      if next_page is not None:
   #          if'catalogue/' in next_page:
   #             next_page_url = 'https://books.toscrape.com/' + next_page
   #          else:
   #             next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
   #          yield scrapy.Request(url = next_page_url, callback = self.parse)
 

   


   #  def parse_book_page(self,response):
   #      table_rows = response.css("table tr")
   #      book_item = BookItem()

     
   #      book_item['url'] =  response.url
   #      book_item['title']= response.css('.product_main h1::text').get()
   #      book_item['upc'] = table_rows[0].css("td ::text").get()
   #      book_item['product_type']= table_rows[1].css("td ::text").get()
   #      book_item['price_excl_tax'] = table_rows[2].css("td ::text").get()
   #      book_item['price_incl_tax']= table_rows[3].css("td ::text").get()
   #      book_item['tax']= table_rows[4].css("td ::text").get()
   #      book_item['availability']=table_rows[5].css("td ::text").get()
   #      book_item['num_reviews']=table_rows[6].css("td ::text").get()
   #      book_item['stars']= response.css("p.star-rating").attrib["class"]
   #      book_item['category']= response.xpath("//ul[@class = 'breadcrumb']/li[@class = 'active']/preceding-sibling::li[1]/a/text()").get()
   #      book_item['description']=response.xpath("//div[@id= 'product_description']/following-sibling::p/text()").get()
   #      book_item['price']=response.css('p.price_color ::text').get()

        
  


        
   #      yield book_item
        # yield {

        #     'url' : response.url,
        #     'title':  response.css('.product_main h1::text').get(),
        #     'product_type': table_rows[1].css("td ::text").get(),
        #     'price_excl_tax' : table_rows[2].css("td ::text").get(),
        #     'price_incl_tax': table_rows[3].css("td ::text").get(),
        #     'tax': table_rows[4].css("td ::text").get(),
        #     'availability':table_rows[5].css("td ::text").get(),
        #     'num_reviews':table_rows[6].css("td ::text").get(),
        #     'stars': response.css("p.star-rating").attrib["class"],
        #     'category':response.xpath("//ul[@class = 'breadcrumb']/li[@class = 'active']/preceding-sibling::li[1]/a/text()").get(),
        #     'description':response.xpath("//div[@id= 'product_description']/following-sibling::p/text()").get(),
        #     'price': response.css('p.price_color ::text').get(),

        # }
import scrapy

class Percival (scrapy.Spider):
    name = 'p'

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def start_requests (self):
        yield scrapy.Request ('https://www.puggina.org/videos?pagina=1')

    def parse (self, response, **kwargs):
        blocos = response.xpath('//div[@class="portfolio-item-active"]//div[@class="portfolio-content"]')
        for bloco in blocos:
            title = bloco.xpath('.//div[@data-mh="titulo-video"]/h4/text()').get()
            date = bloco.xpath('.//div[@data-mh="titulo-video"]/small/text()').get()
            text = bloco.xpath('.//div[@data-mh="texto-video"]//p/text()').get()
            yield {
                    'title': title,
                    'date': date,
                    'text': text
                }
            proxima_pagina = response.xpath('//li[@class="page-item"]//span[text()="Próxima"]/../@href').get()
            if proxima_pagina:
                yield response.follow(proxima_pagina, callback=self.parse)
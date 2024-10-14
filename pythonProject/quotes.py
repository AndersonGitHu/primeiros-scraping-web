import scrapy

# Criação de classe com Spider (para coleta de dados na web)
class Quotes(scrapy.Spider):
    name = 'q'

# Para configurar, em utf-8, os dados a serem extraídos pelo scraping 
    custom_settings = {
        'FEED_EXPORT_ENCODING' : 'UTF-8'
    }

# Função criada com o método start_requests para orientar as requisições do Spider na coleta de dados
    def start_requests(self):
        yield scrapy.Request('https://quotes.toscrape.com/page/1/')

# Função com o método parse para a lógica na extração de dados recebida pelas requisições feitas pelo spider
    def parse(self, response, **kwargs):
            blocos = response.xpath('//div[@class="quote"]')
            for bloco in blocos:
                texto = bloco.xpath('./span[@class="text"]/text()').get()
                author = bloco.xpath('.//small/text()').get()
                tags = bloco.xpath('.//a[@class="tag"]/text()').getall()
                yield {
                    'texto': texto,
                    'author': author,
                    'tags': tags
                }
            proxima_pagina = response.xpath('//li[@class="next"]/a/@href').get()
            if proxima_pagina:
                yield response.follow(proxima_pagina, callback=self.parse)
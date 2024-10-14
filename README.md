**Teste de Web Scraping**

**Target:** https://quotes.toscrape.com/

**Objetivo:**
  Aplicar a técnica de raspagem de dados (scraping) no ambiente web com o intuito de extrair dados como: títulos (titles), tags e textos (text). O site usado foi o Quotes to Scrape (indicado no target acima).

**Configuração do Ambiente:** 
  Gerenciadores/Programas usados:
    Miniconda3
    Python 3.10
    Download pre-built shared indexes
    
  Comandos usados na configuração:
    conda install protego scrapy
    
**Bibliotecas/Ferramentas/Extensões: **
  Scrapy
  iPython
  ipdb
  xPath Helper

**Comandos de instalação das bibliotecas/extensões:**
  conda install protego scrapy 
  pip install ipython
  pip install ipdb
  Extensão xPath Helper instalada no Chrome

**Tutorial do teste de scraping:**
  1- Importar a biblioteca scrapy (import scrapy)
  2- Criação da classe Spider para navegar na web e coletar dados (class Quotes(scrapy.Spider): name = 'q')
  3- Configurar os dados extraídos para o padrão utf-8 (custom_settings = {'FEED_EXPORT_ENCODING': 'utf-8'})
  4- Função start_requests para personalizar as requisições feitas pelo Spider e já com yield scrapy.Request() para essas requisições (def start_requests(self):
        yield scrapy.Request('https://quotes.toscrape.com/page/1/')
  5- Função com método parse para o processamento das requisições spider realizadas, por meio dela será aplicado os laços de repetições e lógica para puxar os dados da maneira pretendida (def parse(self,   response, **kwargs):
  


  

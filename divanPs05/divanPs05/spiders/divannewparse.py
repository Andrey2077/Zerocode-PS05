import scrapy


class DivannewparseSpider(scrapy.Spider):
    name = "divannewparse"
    allowed_domains = ["https://arlight.market"]
    start_urls = ["https://arlight.market/catalog/svetodiodnye-svetilniki-431/"]

    def parse(self, response):
        ligters = response.css('div.slider-hover')

        for ligter in ligters:
            price_main = ligter.css('div.wcard_price .value::text').get(default='').strip()
            price_sup = ligter.css('div.wcard_price .value sup::text').get(default='').strip()
            full_price = f"{price_main}.{price_sup}" if price_sup else price_main
            yield {
                'name': ligter.css('div.wcard__title a::text').get(default='').strip(),
                'price': full_price,
                'url': ligter.css('div.wcard__title a::attr(href)').get(default='').strip()
            }
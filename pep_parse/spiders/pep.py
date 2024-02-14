import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps_url = response.css(
            'section#numerical-index a.pep::attr(href)'
        ).getall()
        all_url = set(all_peps_url)
        for url in all_url:
            yield response.follow(url, callback=self.parse_pep)

    def parse_pep(self, response):
        yield {
            'number': response.css('h1.page-title::text')
            .get()
            .split('–')[0]
            .strip()
            .replace('PEP ', ''),
            'name': response.css('h1.page-title::text')
            .get()
            .split('–')[1]
            .strip(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }

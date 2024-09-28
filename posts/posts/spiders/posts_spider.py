import scrapy
import regex as re


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        # page_number = re.search(r"\d+", response.url).group()
        # filename = f"posts-{page_number}.html"
        # with open(filename, "wb") as f:
        #     f.write(response.body)
        # self.log(f"Saved file {filename}")

        for post in response.css("article.product_pod"):
            yield {
                "title": post.css("h3 > a::text").get(),
                "price": post.css("p.price_color::text").get(),
            }

        next_page = response.css("li.next > a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)

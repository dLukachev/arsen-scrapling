from scrapling.spiders import Spider, Response, Request


class MySpider(Spider):
    name = "get-all-text"
    start_urls = [
        "https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%B2%D0%BE%D1%87%D0%BA%D0%B0_%D0%B8_%D1%84%D0%B0%D1%80%D1%84%D0%BE%D1%80"
    ]
    max_page = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_seen = 0

    async def parse(self, response: Response):
        raw_texts = response.css("p::text").getall()

        cleaned = [t.strip() for t in raw_texts if t.strip()]

        full_text = "\n".join(cleaned)

        self.page_seen += 1

        with open("spider.txt", "a", encoding="utf-8") as f:
            f.write(f"URL: {response.url}\n")
            f.write(full_text)
            f.write("\n\n-----------------------------\n\n")

        yield {
            "url": response.url,
            "text": full_text,
        }

        if self.page_seen < self.max_page:
            for href in response.css("a::attr(href)").getall():
                url = response.urljoin(href)
                yield Request(url=url, callback=self.parse)


if __name__ == "__main__":
    MySpider().start()

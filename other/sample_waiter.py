from scrapling.fetchers import StealthySession

with StealthySession() as session:

    selector = "div[id='products_view_pagination_contents']"

    page = session.fetch("https://catalog-sadovod.ru/", 
                            timeout=10000, 
                            wait_selector=selector)
    
    cards = page.css(selector)

    title = cards[0].css("a[class='product-title']::text")
    print(title[0].text)
    
    
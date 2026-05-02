from scrapling.fetchers import StealthySession

with StealthySession(
    headless=True,
    google_search=False
) as session:
    page = session.fetch("https://www.avito.ru/")
    cards = page.css('div[data-marker="bx-recommendations-block-item"]')

    items = []
    for card in cards:
        title = card.css('a[data-marker="title"]::text').get(default="").strip()
        price_text = card.css('span[data-marker="item-price-value"]::text').get(default="").strip()

        items.append({
            "title": title,
            "price": price_text,
        })

with open('avito.txt', 'a') as f:
    f.write(str(items))

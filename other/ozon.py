from scrapling.fetchers import StealthySession

with StealthySession(
    headless=True, real_chrome=True, user_data_dir="other/profile"
) as session:
    page = session.fetch(
        "https://www.ozon.ru/search/?from_global=true&text=%D1%80%D0%BE%D0%B1%D0%BB%D0%BE%D0%BA%D1%81"
    )
    cards = page.css("div.tile-root")

    items = []
    for card in cards:
        title = card.css(
            "a.tile-clickable-element.v0g_20 span.tsBody500Medium::text"
        ).get(default="")
        price = card.css("span.c35_3_15-a1.tsHeadline500Medium::text").get(default="")

        items.append(
            {
                "title": title,
                "price": price,
            }
        )

with open("other/ozon.txt", "a") as f:
    f.write(str(items))

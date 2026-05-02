from scrapling.fetchers import StealthySession

with StealthySession(
    headless=False,
    real_chrome=True,
    user_data_dir="other/profile"
) as session:
    page = session.fetch("https://catalog-sadovod.ru/")
    
    card = page.css('#products_view_pagination_contents')[0]
    first_item = card.css('.ut2-gl__item')[0]
    link = first_item.css('a.product-title::attr(href)')[0]

    new_page = session.fetch(str(link))
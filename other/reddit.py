from scrapling.fetchers import StealthySession

with StealthySession(headless=True, solve_cloudflare=True) as s:
    page = s.fetch("https://www.reddit.com/")
    titles = page.css("shreddit-post")
    items = []

    for title in titles:
        text = title.css('a[slot="title"]::text').get()
        if text:
            items.append(text)

    with open("reddit.txt", "a") as f:
        f.write(str(items))

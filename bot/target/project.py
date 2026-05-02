from scrapling.fetchers import AsyncStealthySession

async def finder(query: str) -> dict:
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    async with AsyncStealthySession(user_data_dir="other/profile", headless=True, real_chrome=True) as session:
        r = await session.fetch(url, wait_selector="h3")
        titles = r.css("h3::text").getall()
        links_selector = r.css("h3")

    links = []
    for selector in links_selector:
        links.append(selector.parent.css("button[data-testid='favorite-btn']").get())

    response = {}

    for i, (title, link) in enumerate(zip(titles, links)):
        response[i] = (title, link)
    
    return response
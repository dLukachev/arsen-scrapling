from scrapling.fetchers import StealthySession
import time

def finder(query: str):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    with StealthySession(user_data_dir='other/profile', headless=False, real_chrome=True) as session:
        response = session.fetch(url, wait_selector='h3')
        titles = response.css('h3::text').getall()
        links = response.css('h3')

    link_need = []

    for link in links:
        link_need.append(link.parent.css('a::attr(href)').getall())
    
    for i, (title, link) in enumerate(zip(titles, link_need), 1):
        print(f"{i}. {title} - {link}")


if __name__ == "__main__":
    finder('ddrxg', limit=15)
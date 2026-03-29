from scrapling import Fetcher, DynamicFetcher, StealthyFetcher
import requests

response = Fetcher.get("https://gdz.ru/class-11/matematika/bunimovich-bazovyj-i-uglublennyj-uroven/1-1-6/")

element = response.find_all(class_='with-overtask')

img_selector = element[0].css('img')
img_raw = img_selector[0].attrib['src']
print(img_raw)

response_img = requests.get("https:" + img_raw)
with open('other/gdz.jpg', 'wb') as w:
    w.write(response_img.content)
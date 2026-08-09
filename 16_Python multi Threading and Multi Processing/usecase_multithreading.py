'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for responses from servers. Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.
'''

'''
    "https://www.scrapethissite.com/pages/ajax-javascript/#2011",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2012",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2013",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2014",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2015"

'''


from bs4 import BeautifulSoup
import requests
import threading

urls = [
    "https://quotes.toscrape.com/",
    "https://www.scrapethissite.com/pages/forms/",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2010",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2011",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2012",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2013",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2014",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2015"
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()
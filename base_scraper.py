import re
import urllib.request
from bs4 import BeautifulSoup

class BaseScraper:

  def __init__(self, url):
    self.url = url

  def getParser(self):
    response = urllib.request.urlopen(self.url)
    html = response.read()
    return BeautifulSoup(html, 'html.parser')

  def scrape(self):
    soup = self.getParser()

    for table in soup.find_all('table'):
      for tr in table.find_all_next('tr'):
        print(tr.get_text("|", strip=True))

def main():
  scraper = BaseScraper('http://games.espn.com/ffl/livedraftresults')
  scraper.scrape()

if __name__ == "__main__":
  main()
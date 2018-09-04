import re
from base_scraper import BaseScraper

class HarrisTop200(BaseScraper):

  def __init__(self):
    super().__init__('https://www.harrisfootball.com/ranks-top200')

  def scrape(self):
    soup = self.getParser()

    for table in soup.find_all('table'):
      count = 0
      outFile = None
      for tr in table.find_all_next('tr'):
        if count > 200:
          break;
        elif count is 0:
          outFile = open('HarrisTop200' + re.sub(r' ', '', tr.get_text().strip()) + '.csv', 'w')
          outFile.write('Rank,Name,Position,Drafted?\n')
        else:
          row = tr.get_text().strip().replace('\n', ',')
          fields = row.split(',')
          if len(fields) > 3:
            row = fields[0].strip() + ',' + fields[1].strip() + ' ' + fields[2].strip() + ',' + fields[3].strip()
          outFile.write(row + ",N\n")
        count += 1

def main():
  scraper = HarrisTop200()
  scraper.scrape()

if __name__ == "__main__":
  main()
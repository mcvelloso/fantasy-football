import re
from base_scraper import BaseScraper

class EspnTop200(BaseScraper):

  def __init__(self):
    super().__init__('http://games.espn.com/ffl/livedraftresults')

  def scrape(self):
    soup = self.getParser()

    outFile = open('EspnTop200.csv', 'w')
    outFile.write('Rank,Name,Position,ADP,Drafted?\n')

    table = soup.find('table')
    for tr in table.find_all_next('tr'):
      row = tr.get_text(";", strip=True)

      if (re.match(r'\d', row)):
        fields = row.split(';')
        if (len(fields) < 9):
          outFile.write(fields[0] + ',' + fields[1]  + ',' + fields[2] + ',' +  fields[3] + ',N\n')
        else:
          outFile.write(fields[0] + ',' + fields[1]  + ',' + fields[3] + ',' +  fields[4] + ',N\n')

def main():
  scraper = EspnTop200()
  scraper.scrape()

if __name__ == "__main__":
  main()
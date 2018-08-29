from espn_top_200 import EspnTop200
from harris_top_200 import HarrisTop200
import csv

def main():
  # Scrape Harris ranks
  scraper = HarrisTop200()
  scraper.scrape()

  # Scrape ESPN ranks
  scraper = EspnTop200()
  scraper.scrape()

  # Create dict
  dict = {}

  # Iterate over Harris Standard ranks
  with open('HarrisTop200StandardScoring.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        line_count += 1
      else:
        key = (row[1] + ' ' + row[2]).lower()
        dict[key] = {}
        dict[key]['Harris Rank'] = row[0]
        dict[key]['Position'] = row[2]
        dict[key]['Harris Name'] = row[1]
        line_count += 1
    print(f'Processed {line_count} lines.')

  # Iterate over ESPN Top 200
  with open('EspnTop200.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        line_count += 1
      else:
        key = (' '.join(row[1].split(' ')[0:2]) + " " + row[2]).lower()
        if key not in dict:
          dict[key] = {}
        dict[key]['ESPN Rank'] = row[0]
        dict[key]['ESPN Name'] = row[1]
        dict[key]['Position'] = row[2]
        dict[key]['ADP'] = row[3]
        line_count += 1
    print(f'Processed {line_count} lines.')

  print(len(dict))
  outFile = open('FFTop200.csv', 'w')
  outFile.write('Name,Position,Harris Rank,ESPN Rank,ADP,Drafted?\n')
  for key in dict:
    name = ''
    espnRank = '999'
    espnAdp = '999'
    if ('ESPN Name' not in dict[key]):
      name = dict[key]['Harris Name']
    else:
      name = dict[key]['ESPN Name']
      espnRank = dict[key]['ESPN Rank']
      espnAdp = dict[key]['ADP']

    harrisRank = '999'
    if ('Harris Rank' in dict[key]):
      harrisRank = dict[key]['Harris Rank']

    line = name + ','
    line += dict[key]['Position'] + ','
    line += harrisRank + ','
    line += espnRank + ','
    line += espnAdp + ',0\n'

    outFile.write(line)

if __name__ == "__main__":
  main()
import sys
sys.path.append('../')
from source import scraper
import datetime

weedmaps_json_site = "https://api-g.weedmaps.com/discovery/v1/listings?sort_by=position&filter%5Blocation%5D=any&latlng=33.96210098266602%2C-118.2745513916016&page_size=100&page=1"
source = "WEEDMAPS"
current = datetime.datetime.now()
date = current.strftime("%m-%d-%Y")

weedmap = scraper.scraper(weedmaps_json_site, source)
weedmap.connect()
weedmap.parse()
weedmap.output("weedmaps-" + date + ".csv")

print("All Done")

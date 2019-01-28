from src.extractor import Extractor as Extract
from src.pracuj_scrapper import PracujScrapper as Pracuj_Scrapper
from src.utils import dict2csv, clearCsv


with open("keywords.txt") as f:
    keywords = f.readlines()

keywords = [x.strip() for x in keywords]
location = 'slaskie'

clearCsv()

for keyword in keywords:

    Extractor = Extract(keyword.replace(" ", "%20"), location)
    soup = Extractor.scrapWebsite()

    scrap_pracuj = Pracuj_Scrapper(soup)
    dicts = scrap_pracuj.cleanTitles()

    dict2csv(dicts)

    print(f"Collecting data for: {keyword}")


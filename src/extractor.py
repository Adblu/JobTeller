import requests
from bs4 import BeautifulSoup


class Extractor:

    def __init__(self, keyword, location):
        self.keyword = keyword
        self.location = location

    def getLink(self):
        return 'https://www.pracuj.pl/praca/' + self.keyword + ';kw/' + self.location + ';wp'


    def scrapWebsite(self):
        try:
            page = requests.get(Extractor.getLink(self))
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup

        except:
            raise ValueError('Broken link. Please check the link.')



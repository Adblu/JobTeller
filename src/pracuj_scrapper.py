import re
import ast


class PracujScrapper:

    def __init__(self, soup):
        self.soup = soup
        self.filtered = []
        self.list_of_scripts = []
        self.single_data = []

    def searchHtml(self):
        self.list_of_scripts = self.soup.find_all("script")

    def html2str(self):
        single_data = []
        for x in self.list_of_scripts:
            single_data.append(str(x))
        self.single_data = single_data

    def search4titles(self):
        for row in self.single_data:
            search_result = re.search('{"@context":"http://schema.org/","@type":"JobPosting","title":"', row)
            found = (not (search_result is None))
            if found:
                self.filtered.append(row)
        self.filtered = self.filtered[1:]

    def cleanTitles(self):
        PracujScrapper.searchHtml(self)
        PracujScrapper.html2str(self)
        PracujScrapper.search4titles(self)
        dicts = []
        for entry in self.filtered:
            a, b = entry.find('{"@'), entry.find('}} ')
            single_dict = entry[a:b] + '}}'

            aa = ast.literal_eval(single_dict)
            dicts.append(aa)
        return dicts

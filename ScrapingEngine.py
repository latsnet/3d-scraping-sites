from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError

from models import *

class ScrapingEngine(object):

    def __init__(self, site):
        self.site = site
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        self.__file_name = site + ".txt"

    def manage_html(self, html):
        return ' '.join(html.decode('utf-8').split()).replace("> <", "><")

    def start_scrapping(self):
        self.file = open(self.__file_name, 'w')
        print('Start scrapping site %s' % (self.site))

    def save_model(self, model):
        # Routine to save information
        self.file.write("Saving model: " + model.description)

    def end_scrapping(self):
        self.file.close()

    def get_page_content(self, url):
        try:
            req = Request(url, headers = self.headers)
            response = urlopen(req)
            html = response.read()
            return self.manage_html(html)

        except HTTPError as e:
            print(e.status, e.reason)
            return ""

        except URLError as e:
            print(e.reason)
            return ""
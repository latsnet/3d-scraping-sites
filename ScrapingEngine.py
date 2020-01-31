from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
import json

from models import *

class ScrapingEngine(object):

    def __init__(self, site):
        self.site = site
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        self.__file_name = "./output/data/" + site + ".txt"

    def manage_html(self, html):
        return ' '.join(html.decode('utf-8').split()).replace("> <", "><")

    def start_scrapping(self):
        self.file = open(self.__file_name, 'w')
        print('Start scrapping site %s' % (self.site))

    def save_model(self, model):
        # Routine to save information
        json_model = json.dumps(model)
        self.file.write(json_model + "\n")
        print(json_model)

    def end_scrapping(self):
        self.file.close()

    def get_page_content(self, url):
        html = ""
        while True:
            try:
                req = Request(url, headers = self.headers)
                response = urlopen(req)
                html = response.read()
                if (html is not ""):
                    break

            except HTTPError as e:
                print(e.status, e.reason)

            except URLError as e:
                print(e.reason)

        return html
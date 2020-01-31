from ScrapingEngine import ScrapingEngine
from models import Model3D
from bs4 import BeautifulSoup

class ScrapThingiverse(ScrapingEngine):

    def __init__(self):
        self.__base_url = "https://www.thingiverse.com/newest"
        super(ScrapThingiverse, self).__init__('thingiverse')

    def start_scrapping(self):
        print("Beggining Thingiverse")

        super(ScrapThingiverse, self).start_scrapping()

        self.load_pages()

        super(ScrapThingiverse, self).end_scrapping()

        print("Ok Thingiverse")

    def get_url_page(self, page):
        if (page > 1):
            return self.__base_url + "/page:" + str(page)
        else:
            return self.__base_url

    def load_pages(self):
        page = 1
        number_of_models = 0

        while True:
            url = self.get_url_page(page)
            print("Loading %s" % (url))

            html = super(ScrapThingiverse, self).get_page_content(url)
            soup = BeautifulSoup(html, 'html.parser')

            print("Page %s" % (page))
            cards = soup.findAll("div", {"class": "thing-card"})
            for card in cards:
                model = {}
                info = card.find("div", {"class": "item-info"})

                model["title"] = card.get("title")
                model["url"] = "https://www.thingiverse.com" + info.find("a").get("href")
                self.load_details(model)

                self.save_model(model)

                number_of_models += 1
                print("Number of models: %s" % (number_of_models))

            page+=1

    def load_details(self, model):
        print("Loading content of " + model["url"])
        html_content = super(ScrapThingiverse, self).get_page_content(model["url"])

        soup = BeautifulSoup(html_content, 'html.parser')
        model["details"] = soup.find("div", {"id": "description"}).div.p.getText()

        # Tags
        info_tags = soup.find("div", {"class": "taglist"}).findAll("a")
        tags = []
        for info in info_tags:
            tags.append(info.getText())
        model["tags"] = tags

        # Licenses
        info_licenses = soup.find("div", {"class": "cc-licenses"}).findAll("img")
        licenses = []
        for info in info_licenses:
            licenses.append(info.get("src").split("_")[-1])
        model["licenses"] = licenses

        
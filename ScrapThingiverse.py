from ScrapingEngine import ScrapingEngine
from models import Model3D
from bs4 import BeautifulSoup

class ScrapThingiverse(ScrapingEngine):

    def __init__(self):
        self.__base_url = "https://www.thingiverse.com/newest"
        super(ScrapThingiverse, self).__init__('Thingiverse')

    def start_scrapping(self):
        print("Beggining Thingiverse")

        super(ScrapThingiverse, self).start_scrapping()

        self.load_pages()

        # model = Model3D("http://Thingiverse.com", "description_test", "full_description_test", "various", ["3D", "figure"])
        # super(ScrapThingiverse, self).save_model(model)

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
        while (page < 10):
            url = self.get_url_page(page)
            print("Loading %s" % (url))
            html = super(ScrapThingiverse, self).get_page_content(url)
            if (html is not ""):
                soup = BeautifulSoup(html, 'html.parser')

                print("Page %s" % (page))
                cards = soup.findAll("div", {"class": "thing-card"})
                for card in cards:
                    print(" -> " + card.get("title"))
                    info = card.find("div", {"class": "item-info"})
                    url = info.find("a")
                    number_of_models += 1

            page+=1

        print("Number of models: %s" % (number_of_models))


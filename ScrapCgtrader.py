from ScrapingEngine import ScrapingEngine
from models import Model3D

class ScrapCgtrader(ScrapingEngine):

    def __init__(self):
        self.__base_url = "https://cgtrader.com/en/categories/"
        super(ScrapCgtrader, self).__init__('cgtrader')

    def start_scrapping(self):
        print("Beggining CGTrader")

        super(ScrapCgtrader, self).start_scrapping()

        self.load_category("art")
        self.load_category("fashion")

        # model = Model3D("http://cgtrader.com", "description_test", "full_description_test", "various", ["3D", "figure"])
        # super(ScrapCgtrader, self).save_model(model)

        super(ScrapCgtrader, self).end_scrapping()

        print("Ok cgtrader")

    def get_url_category(self, category, page):
        if (page > 1):
            return self.__base_url + category + "?page=" + str(page)
        else:
            return self.__base_url + category

    def load_category(self, category):
        page = 1
        while (page < 10):
            url = self.get_url_category(category, page)
            print("Loading %s" % (url))
            html = super(ScrapCgtrader, self).get_page_content(url)
            if (html is not ""):
                print("Page %s" % (page))
            
            page+=1


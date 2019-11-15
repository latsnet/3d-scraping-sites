from ScrapingEngine import ScrapingEngine
from models import Model3D

class ScrapCults3D(ScrapingEngine):

    def __init__(self):
        self.__base_url = "https://cults3d.com/en/categories/"
        super(ScrapCults3D, self).__init__('Cults3D')

    def start_scrapping(self):
        print("Beggining Cults3D")

        super(ScrapCults3D, self).start_scrapping()

        self.load_category("art")
        self.load_category("fashion")

        # model = Model3D("http://cults3d.com", "description_test", "full_description_test", "various", ["3D", "figure"])
        # super(ScrapCults3D, self).save_model(model)

        super(ScrapCults3D, self).end_scrapping()

        print("Ok Cults3D")

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
            html = super(ScrapCults3D, self).get_page_content(url)
            if (html is not ""):
                print("Page %s" % (page))
            
            page+=1


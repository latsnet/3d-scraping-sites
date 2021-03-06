from ScrapingEngine import ScrapingEngine
from models import Model3D

class ScrapYeggi(ScrapingEngine):

    def __init__(self):
        self.__base_url = "https://yeggi.com"
        super(ScrapYeggi, self).__init__('yeggi')

    def start_scrapping(self):
        print("Beggining yeggi")

        super(ScrapYeggi, self).start_scrapping()

        self.load_pages()

        # model = Model3D("http://yeggi.com", "description_test", "full_description_test", "various", ["3D", "figure"])
        # super(ScrapYeggi, self).save_model(model)

        super(ScrapYeggi, self).end_scrapping()

        print("Ok yeggi")

    def get_url_page(self, page):
        if (page > 1):
            return self.__base_url + "/new/" + str(page) + "/"
        else:
            return self.__base_url

    def load_pages(self):
        page = 1
        while (page < 10):
            url = self.get_url_page(page)
            print("Loading %s" % (url))
            html = super(ScrapYeggi, self).get_page_content(url)
            if (html is not ""):
                print("Page %s" % (page))
            
            page+=1


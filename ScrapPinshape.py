from ScrapingEngine import ScrapingEngine
from models import Model3D

class ScrapPinshape(ScrapingEngine):

    def __init__(self):
        super(ScrapPinshape, self).__init__('Pinshape')

    def start_scrapping(self):
        print("Beggining Pinshape")

        super(ScrapPinshape, self).start_scrapping()

        model = Model3D("http://pinshape.com", "description_test", "full_description_test", "various", ["3D", "figure"])
        super(ScrapPinshape, self).save_model(model)

        super(ScrapPinshape, self).end_scrapping()

        print("Ok Pinshape")

from ScrapingEngine import ScrapingEngine
from models import Model3D

class ScrapCults3D(ScrapingEngine):

    def __init__(self):
        super(ScrapCults3D, self).__init__('Cults3D')

    def start_scrapping(self):
        print("Beggining Cults3D")

        super(ScrapCults3D, self).start_scrapping()

        model = Model3D("http://cults3d.com", "description_test", "full_description_test", "various", ["3D", "figure"])
        super(ScrapCults3D, self).save_model(model)

        super(ScrapCults3D, self).end_scrapping()

        print("Ok Cults3D")

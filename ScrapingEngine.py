from models import *

class ScrapingEngine(object):

    def __init__(self, site):
        self.site = site
        self.__file_name = site + ".txt"

    def start_scrapping(self):
        self.file = open(self.__file_name, 'w')
        print('Start scrapping site %s' % (self.site))

    def save_model(self, model):
        # Routine to save information
        self.file.write("Saving model: " + model.description)

    def end_scrapping(self):
        self.file.close()
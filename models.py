# -*- coding: UTF-8 *-*

class Model3D(object):
    'Class for 3D models'

    def __init__(self, full_url, description, full_description, category, tags):
        self.full_url = full_url
        self.description = description
        self.full_description = full_description
        self.category = category
        self.tags = tags
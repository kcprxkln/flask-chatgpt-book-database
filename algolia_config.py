import os

class AlgoliaConfig():

    def __init__(self):
        self.apikey = os.getenv("algolia_apikey")
        self.app_id = os.getenv("algolia_app_id")
        self.index = os.getenv("init_index")

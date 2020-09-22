from user.service import Service
from user.entity import Entity

class Controller:
    def __init__(self):
        self.service = Service()
        self.entity = Entity()

    def preprocessing(self):
        pass

    def modeling(self):
        pass

    def learning(self):
        pass

    def submit(self):
        pass


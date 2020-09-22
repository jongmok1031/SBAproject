import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from crawler.entity import Entity
from crawler.service import Service


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

if __name__ == '__main__':
    api = Controller()
    service = Service()
    service.naver_cartoon('https://comic.naver.com/webtoon/weekday.nhn')

print('s')
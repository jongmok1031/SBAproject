import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from crawler.entity import Entity
from crawler.service import Service


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
    

if __name__ == '__main__':

    service = Service()

    myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
    service.open_url(myurl)  

    myfolder = "C:\\Users\\jongm\\SBAprojects\\crawler\\navercartoon\\"
    service.create_folder_week(myfolder)
    
    tag = 'div'
    class_attrs = 'thumb'
    service.mytarget(myurl,tag,class_attrs)

    href_replacement='/webtoon/list.nhn?'
    service.makelist(myurl,href_replacement,myfolder,tag,class_attrs)


    csvfilename = 'cartoon.csv'
    mycols = ['타이틀번호', '요일', '제목', '링크']
    weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}

    api = Controller()
    api.naver_cartoon_crawler(myurl,myfolder,tag,class_attrs,href_replacement,mycols,csvfilename)
print('s')
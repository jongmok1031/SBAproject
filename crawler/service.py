import sys
import os
import shutil
sys.path.insert(0,'/Users/jongm/SBAprojects')
from crawler.entity import Entity
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np

class Service:
    def __init__(self):
        self.entity = Entity()
        self.weekday_dict = None
        self.mylist=None
        self.mysoup =None
    def bugs_music(self):
        pass

    def naver_movie(self):
        pass


    def open_url(self, myurl):
        myparser = 'html.parser' # html.parser : 간단한 HTML과 XHTML 구문 분석기. 표준 라이브러리
        #myurl # 원래는 'https://comic.naver.com/webtoon/weekday.nhn'
        response = urlopen(myurl)
        mysoup = BeautifulSoup(response, myparser)
        return mysoup


        # 요일별 폴더 생성
    def create_folder_week(self, myfolder):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
        self.weekday_dict = weekday_dict
     
        # myfolder # 예시 : C:\Users\jongm\SBAprojects\crawler\navercartoon\
        # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)
            print('파일이미존재함')
    
    # 먼저 target 잡아주는 함수
    def mytarget(self,myurl,tag,class_attrs):
        mysoup = self.open_url(myurl)
        target = mysoup.find_all(tag, attrs = {'class': class_attrs})

        return target
        #target = self.soup.find_all('div', attrs = {'class':'thumb'})

    
  
    # 만화 항목들과 그에 맞는 요약본,이미지를 저장
    def makelist(self,myurl,href_replacement,myfolder,tag,class_attrs):
        self.mylist = []
        for abcd in self.mytarget(myurl,tag,class_attrs):
    
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace(href_replacement,'')
            result = myhref.split('&')
            # print(myhref)
            # print(result)
            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]
            #print(mytitleid,myweekday)

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?','').replace(':','').replace('!','')

            mysrc = imgtag.attrs['src']
            #print(mytitle,mysrc)

            Service.saveFile(mysrc,myweekday,mytitle,myfolder)

            sublist =[]
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)

            self.mylist.append(sublist)
        Service.SaveCsv(csvfilename, mycols)

    # 각 이미지를 저장해주는 함수
    @staticmethod
    def saveFile(mysrc, weekday_dict, mytitle,myfolder):
        image_file = urlopen(mysrc) # mysrc위에서 나와야함

        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
        # print(mysrc)
        # print(filename)

        myfile = open(filename, mode='wb') # wb : write binary
        myfile.write(image_file.read()) # 바이트 형태로 저장
        myfile.close()

   
    #csv로 저장
    @staticmethod
    def SaveCsv(csvfilename,mycols):
        myframe = pd.DataFrame(self.mylist, columns = mycols)
        filename = csvfilename
        myframe.to_csv(filename, encoding='utf-8',index=False)
        print(filename+'파일이 저장됨')
        print('finished')

#     def frommovie(soup,tag,class_attrs,mycol):
        
# tags = soup.findAll('div', attrs={'class':'tit3'})
# # print(tags)
# for tag in tags:
#     print(tag.a.string)
# print('**************************')
# print('<a> 태그의 href 전체 태그')
# url_header = 'https://movie.naver.com'
# for tag in tags:
#     print(url_header + tag.a['href'])

# mytrs = soup.find_all('tr')
# print(len(mytrs))

# no=0 #순서를 의미하는 번호
# total_list = [] # 전체를 저장할 리스트

# for one_tr in mytrs:
#     title = ''
#     up_down = ''
#     mytd = one_tr.find('td',attrs = {'class':'title'})
#     if mytd != None:
#         no+=1
#         newno = str(no).zfill(2)

#         mytag = mytd.find('div',attrs = {'class':'tit3'})
#         #.string속성 : 해당 태그가 갖고 있는 문자열 출력
#         title = mytag.a.string

#         # td 태그 중에서 3번쨰 요소를 찾기
#         mytd = one_tr.select_one('td:nth-of-type(3)')
#         myimg = mytd.find('img')
#         if myimg.attrs['alt'] == 'up':
#             up_down='상승'
#         elif myimg.attrs['alt'] == 'down':
#             up_down = '강등'
#         else:
#             up_down = '불변'

#         change = one_tr.find('td', attrs={'class':'range ac'})
#         change = change.string

#         #print(newno + '/' + title + '/' + up_down + '/' + change)
#         total_list.append((newno,title,up_down,change))

# mycol = ['순위','제목','변동','변동값']
# mydataframe = pd.DataFrame(total_list, columns= mycol)

# filename = 'naverMovie.csv'
# mydataframe.to_csv(filename, encoding='utf-8',index=False)

# print(mydataframe.head(5))
# print(filename +'저장')
# print('finished')
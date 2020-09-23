import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
import re
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import pandas as pd
from nltk import FreqDist
#from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from miner.entity import Entity
from gensim.models import word2vec
from bs4 import BeautifulSoup
from konlpy.tag import Okt

class Service:
    def __init__(self):
        self.entity =Entity()
        
    def openfile_as_soup(self, filename):
        this = self.entity
        this.filename = filename # '문재인대통령신년사.txt'
        myfile = open(this.filename, 'rt', encoding='utf-8')
        soup = BeautifulSoup(myfile, 'html.parser')
        mydata = soup.text
        return mydata

    @staticmethod
    def import_okt(text):
        okt=Okt()
        return okt.pos(text, norm=True, stem=True)

    def read_data(self, mydata,filename):
        filename = self.entity.filename
        service = Service()
        mydata = service.openfile_as_soup(filename)
        datalines = mydata.split('\n')
        for oneline in datalines:
            mypos = Service.import_okt(oneline)
        return mypos
    @staticmethod
    def append_words(pos):
        results = [] #결과 여기에 저장
        imsi=[]
        for word in pos:
            if not word[1] in ['Josa','Eomi','Punctuation','verb']:
                if len(word[0])>=2:
                    imsi.append(word[0])
        temp = (' '.join(imsi)).strip()
        results.append(temp)
        return results

    @staticmethod
    def savefile(results,prepro_file):
        prepro_file = 'word2vec.prepro'
        with open(prepro_file,'wt',encoding='utf-8') as myfile:
            myfile.write('\n'.join(results))
        print(prepro_file + '생성됌')
        return prepro_file
        

    @staticmethod# linesentence 분석을 하기위한 sentence를 만들어주는 함수
    def sentence_creator(prepro_file,filename):
        data = word2vec.LineSentence(prepro_file)
        # word2vec  :해당 sentence를 이용하여 word2vec에대한 모델을 생성
        # size: 벡터 차원수  window :윈도우 사이즈, (앞뒤로 window만큼)   mincount: 버리고자 하는 최소빈도수
        # sg:  1(skipgram), 0(cbow)
        print(type(data))
        return data
    
    @staticmethod
    def model_creator(data,model_filename,prepro_file,filename):
        data = Service.sentence_creator(prepro_file,filename)
        model = word2vec.Word2Vec(data,size=200, window=10, min_count=2, sg=1)
        #model_filename= 'word2vec.model'
        # 모델을 저장할떄는 modelname.save  .save 함수 사용
        # 모델 파일은 바이트 형식의 파일임
        print(type(model))
        model.save(model_filename)
        print(model_filename + '파일 생성됌')
        print('finished')
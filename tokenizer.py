import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
 
import pandas as pd 
import numpy as np
from konlpy.tag import Okt
# from konlpy.tag import Kkma 시간 오래걸려


class Tokenizer():
    def __init__(self):
        self.okt = Okt() 
        
    def stopwords(self):
        f= open('불용어.txt','r', encoding='utf8')
        stopwords = f.read()
        f.close()
        return stopwords

    def hook_process(self):
        df = self.get_data()
        self.tokenize(df)
        
    def get_data(self):
        review_data = pd.read_csv(os.path.join(basedir,  '앱리뷰csv파일.csv'))
        return review_data.head(5)
 
    def tokenize(self,df):
        df = self.get_data()
        for line in df['review']:
            print(self.okt.pos(line))  
        # return (self.okt.pos(line))

if __name__ == "__main__":
    Tk = Tokenizer()
    Tk.hook_process()
    stopwords = Tk.stopwords()
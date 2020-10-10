import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
 
import pandas as pd 
import numpy as np
from konlpy.tag import Okt


class Tokenizer():
    def __init__(self):
        self.okt = Okt()
        pass

    def hook_process(self):
        #df = wc.webdata_toCsv(urls)
        wc.add_sentiment(df)
        self.get_data()

    def get_data(self):
        review_data = pd.read_csv(os.path.join(basedir,  '앱리뷰csv파일.csv'))
        print(review_data.head())
        return review_data
 
    def tokenize(self,df):
        df = pd.read_csv(os.path.join(basedir,'앱리뷰csv파일.csv'), encoding = 'utf-8')
        print(self.okt.pos(df['review'][1]))

if __name__ == "__main__":
    tk = Tokenizer()
    df = pd.read_csv(os.path.join(basedir,'앱리뷰csv파일.csv'), encoding = 'utf-8')
    tk.tokenize(df)
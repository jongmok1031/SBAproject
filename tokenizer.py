import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
 
import pandas as pd 
import numpy as np
from konlpy.tag import Okt

from util.file_helper import FileReader
from fromweb import WebCrawler as wc
# from konlpy.tag import Kkma 시간 오래걸려


class Tokenizer():
    def __init__(self):
        self.wordtoken_list = []
        self.reader = FileReader()
        self.okt = Okt()
        self.df = self.get_data()

    def hook_process(self): 
        df = self.df
        self.stopwords = self.get_stopwords()
        self.word_tokens = self.tokenize(df)
        
    def get_stopwords(self):
        f= open('불용어.txt','r', encoding='utf8')
        stopwords = f.read()
        f.close()
        return stopwords
    
    def remove_stopwords(self, word_tokens):
        word_tokens = self.word_tokens
        stopwords = self.stopwords
        
        print('-===================')
        print(word_tokens)
        print('-===================')
        for morphset in word_tokens:
            print(morphset)
            print('123')
        #     for morph in morphset:
        #         if morph in stopwords:
        #             morphset.remove(morph)
        # return word_tokens


    def get_data(self): 
        reader = self.reader
        reader.context = basedir
        reader.fname = "앱리뷰csv파일.csv"
        reader.new_file()
        review_data = reader.csv_to_dframe()
        return review_data.head(2)
 
    def tokenize(self,df):
        df = self.df
        for line in df['review']:
            print(self.okt.morphs(line))  
        return (self.okt.morphs(line))

if __name__ == "__main__":
    Tk = Tokenizer()
    Tk.hook_process() 
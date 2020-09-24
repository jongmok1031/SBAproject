import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from util.file_handler import FileReader
import pandas as pd
import numpy as np

# entity랑 서비스 합칠꺼야 모델로
class Model:
    def __init__(self):
        self.fileReader = FileReader()
    def new_model(self, payload):
        this = self.fileReader
        this.context = '/Users/jongm/SBAprojects/price_prediction/data/'
        this.fname = payload 
        return pd.read_csv(this.context + this.fname)


if __name__ =='__main__':
    m = Model()
    df = m.new_model('price_data.csv')
    print(df.head())

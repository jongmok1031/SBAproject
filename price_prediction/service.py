import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
import pandas as pd
from cabbage.entity import Entity

class Service:
    def __init__(self):
        self.entity =Entity()
    
    def new_model(self,datafile):
        this = self.entity
        this.fname = datafile
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_label(this):
        pass  

    @staticmethod
    def create_feature(this):
        pass

    @staticmethod
    def to_integer(this):
        # 학습가능하게 정수로..
        pass
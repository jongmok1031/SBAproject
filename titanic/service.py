import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from titanic.entity import Entity
import pandas as pd
import numpy as np 


"""
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

class Service:
    def __init__(self):
        self.entity = Entity()
    
    def new_model(self,payload):
        this = self.entity

        this.fname = payload
        return pd.read_csv(this.context + this.fname)   # 교과서 p.139  df = tensor

    @staticmethod 
    def create_train(this) -> object :
        return this.train.drop('Survived', axis = 1)  # train은 답이 제거된 데이터셋

    @staticmethod
    def create_label(this) -> object :
        return this.train['Survived'] # label - 답        feature=variables

    @staticmethod
    def drop_feature(this,feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis= 1) #p.149보면 train,test로 split
        return this
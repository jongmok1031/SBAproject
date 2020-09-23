import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from titanic.entity import Entity
import pandas as pd
import numpy as np 


"""
PassengerId  고객ID, @@@문제
Survived 생존여부,  @@@답

Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Fare 요금,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼

###########Ticket 티켓번호,
###########Cabin 객실번호,
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
    def create_label(this) -> object :  #categorical
        return this.train['Survived'] 
        ######### label - 답        feature=variables

    @staticmethod
    def drop_feature(this,feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis= 1) #p.149보면 train,test로 split
        return this

    @staticmethod
    def pclass_ordinal(this) ->object:
        return this

    @staticmethod
    def name_nominal(this)->object:
        return this

    @staticmethod
    def title_nominal(this) ->object:
        combine = [this.train, this.test]
        for dataset in combine : 
            dataset['Title'] = dataset['Name'].str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess','Lady','Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Ms','Miss')
            dataset['Title'] = dataset['Title'].replace('Mlle','Mr')
        title_mapping = {'Mr':1,'Miss':2,'Mrs':3,'Master':4,'Royal':5,'Rare':6}
        for dataset in combine: 
            dataset['Title'] = dataset['Title'],map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0) #Unknown
        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def sex_nominal(this) ->object:
        combine = [this.train, this.test]
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)

        this.train = this.train #overriding
        this.test = this.test 
        return this
    
    @staticmethod
    def age_ordinal(this)->object:
        train = this.train
        test = this.test 
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
         # age는 뭐라 넣기가 애매함, 그리고 가중치가 크니까 신중해야대 
        bins = [-1,0,5,12,18,24,35,60, np.inf] #이건 변수명이야 []안에있자나
        labels= ['Unknown','Baby','Child','Teenager','Student','Young Adult','Adult','Senior']
        train['AgeGroup'] = pd.cut(train['Age'],bins,labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'],bins,labels=labels)
        #이렇게 [] 에서 {}으로 처리하면 labels을 값으로 처리
        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x]=='Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x]=='Unknown':
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]

        age_title_mapping = {
            Unknown:0,
            Baby:1,
            Child:2,
            Teenager:3,
            Student:4,
            Young Adult:5,
            Adult:6,
            Senior:7
        } 
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test 
        
        return this
    
    @staticmethod
    def sibsp_numeric(this)->object:
        return this

    @staticmethod
    def parch_numeric(this)->object:
        return this
    
    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        return this


    @staticmethod
    def fareBand_nominal(this)->object:  #요금이 다양하니 클러스터링을 하기위한 준비
        this.train = this.train.fillna({'FareBand' : 1})  # FareBand라는 변수추가
        this.test = this.test.fillna({'FareBand' : 1})
        return this

    @staticmethod
    def embarked_nominal(this)->object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        # ml library assumes class label in Z
        # 교과서 146 문자 blue=0 green=1 red=2 로 치환
        this.train['Embarked'] = this.train['Embarked'].map({'S':1,'C':2,'Q',3})
        this.test['Embarked'] = this.test['Embarked'].map({'S':1,'C':2,'Q',3})
        # ordinal 아님
        return this
import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
from titanic.service import Service
from titanic.entity import Entity

class Controller:
    def __init__(self):
        self.service = Service()
        self.entity = Entity()
 
    def modeling(self,train,test):
        service = self.service
        this = self.preprocessing(train,test)
        print(f'훈련 컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocessing(self,train,test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train)  #payload
        this.test = service.new_model(test)  #payload
        this.id = this.test['PassengerId'] #machine에게 question이됌
        print(f'드롭 전 변수: {this.train.columns}')
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        print(f'드롭 후 변수: {this.train.columns}')
        return this

   


    def learning(self):
        pass

    def submit(self): #machine이 된다. 캐글에게 내 머신을 보내서 평가받는것
        pass

if __name__ =='__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv','test.csv')
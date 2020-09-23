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


        this = service.embarked_nominal(this)
        print(f'승선한 항구 정제결과:\n{this.train.head()}')
        this = service.title_nominal(this)
        print(f'타이틀 정제결과:\n{this.train.head()}')
        # name변수에서 title을 추출했으니 name은 필요가 없어짐
        # str이니, 후에 ML-lib 가 이를 인식하는 과정에서 에러낼꺼임
        # 삭제해야댐
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        print(f'나이 정제결과: \n {this.train.head()}')
        this = service.sex_nominal(this)
        print(f'성별 정제결과: \n {this.train.head()}')
        this = service.fareBand_nominal(this)
        print(f'요금 정제결과: \n {this.train.head()}')
        this = service.drop_feature(this, 'Fare')
        print(f'전체 정제결과: \n {this.train.head()}')
        print(f'train na 체크: \n {this.train.isnull().sum()}')
        print(f'test na 체크: \n {this.test.isnull().sum()}')

        return this

   


    def learning(self,train,test):
        service = self.service
        this = self.modeling(train,test)
        print('=====================  Learning 결과 ===================')
        print(f'결정트리 검증결과: {service.accuracy_by_dtree(this)}')
        print(f'램덤포레스트 검증결과: {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과: {service.accuracy_by_nb(this)}')
        print(f'knn 검증결과: {service.accuracy_by_knn(this)}')
        print(f'svm 검증결과: {service.accuracy_by_svm(this)}')
        


        

    def submit(self): #machine이 된다. 캐글에게 내 머신을 보내서 평가받는것
        pass

if __name__ =='__main__':
    ctrl = Controller()
    ctrl.learning('train.csv','test.csv')
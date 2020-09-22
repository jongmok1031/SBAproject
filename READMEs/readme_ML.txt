Machine Learning

type : 지도, 비지도, 강화

process : 
    preprocessing
    modeling
    learning
    evaluation

algorithm :
    1. perceptron -> neuron
    2. 회귀 regression
    3. 분류 classification
    4. SVM (support vector matrix)
    5. Decision tree
    6. Kmean clssifier
    7. PCA (principal component analysis)
    8. R-forest (a type of ensemble)   -> RF
    9. NLP 
    10. Deep Learning  -> DL

여기까지가 머신러닝 교과서 ch13.

Tensorflow 

---------
비지니스로직 - service
processing을 하는 파일명
    preprocessing
    modeling
    learning, evaluation
    완성되면 submit(파일로저장)

# 외부에 있는 파이썬 파일을 import해야 속성,기능을 사용할수있음
# 내부에서는 이걸 인스턴스화 해야한다
# entity = Entity()
# 인스턴스 = 클래스().   소문자가 인스턴스, 객체로 정의.
# ()가 있는 Entity() 는 생성자라고 한다.

# 객체지향(OOP)에서는 속성과 기능을 호출하는 구조로 2가지 방식
# calc = Calculator()  example
# calc 는 인스턴스 객체
# Calculator 는 클래스 객체(스태틱)이라고 함
# calc.sum() 하면 인스턴스 호출방식 --다이나믹
# Calculator.sum() 하면 클래스 호출방식 -- 스태틱

from titanic.service import Service
from titanic.entity import Entity
class Controller:
    def __init__(self):
        self.service = Service()
        self.entity = Entity()

============

페이로드  : 전송되는 데이터

this.fname = payload - > setter 할당연산자(=)있으면 setter
this.fname 만 있으면 getter =없으면 getter

==============

PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked  - 메타데이터= 스키마 = feature = variables= properties= attributes
892,3,"Kelly, Mr. James",male,34.5,0,0,330911,7.8292,,Q  - row, 행, 인스턴스, raw데이터
893,3,"Wilkes, Mrs. James (Ellen Needs)",female,47,1,0,363272,7,,S
894,2,"Myles, Mr. Thomas Francis",male,62,0,0,240276,9.6875,,Q
====================

차원(dim)

variable x=3 스칼라, 0 차원
array    []  = {1,2,3} 벡터, 1차원, array내부의variable 는 element가 됌
matrix [[]]  = {{1,2,3},{4,5,6}} matrix 2dim, dataframe, tensor. 
===========
지도학습 : 반드시 dataset 생성해야함. 
            이를 train, test로 split 필수



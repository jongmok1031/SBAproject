클래스 하나가 단위unit
이제 확장 진행...
객체 지향에서는 디자인 패턴이라는 개념 존재

패턴 조합을 통해 큰 개념의 패턴 -> MVC 패턴
model, view, controller, 의 조합, java,c 에서 주로 사용

model : 데이터처리 -> API 서버 Python -> Tensorflow
view : 화면 ui 처리  -> ui서버 Reactjs
controller : model, view 연결 --> 네트워크처리 Flask : (app.py)  -> RESTful 방식

backend tier (api 서버 구축담당: java, c, python sql)
frontend tier (ui 서버 구축담당 : javascript, html, reactjs)

모델 제작, 뷰 만들고, 컨트롤러로 연결...의 반복
프로토타입

독자적으로 움직이는--> 모듈
5개의 모듈(각 개인이 작성) 

titanic 폴더에 데이터셋 존재
entity(속성) + service(기능) = 객체(object)

def __init__(self, ...)=>속성
def abc() : -> 기능 function
결국 class는 객체를 정의하는 것

class 가 여러개( entity, service ) 가 모여서 큰개념의 객체를 이룸
얘는 클래스라 하지 않고 model 이라고함

패키지는 같은 컨셉을 공유하는 클래스의 집합 ... 모듈..--> 모델
모델에 ai 개념 없으면 web에서 말하는 모델
ai 개념잇으면 인공지능모델

ai 개념 = 머신러닝 코딩의 유무
dataset을 추가하면 지도학습, 없으면 비지도학습
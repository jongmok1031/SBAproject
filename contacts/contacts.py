class Contact:
    def __init__(self,name,phone,email,addr): # ()안에 속성저장. 객체생성
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr
    
    def print_info(self):  #동적 self잇음 dynamic  #메소드가 유효한 시간동만만 존재. 그 메소드가 소멸된후 값은 self에 저장
        print(f'이름 : {self.name}, 전화번호: {self.phone}, 이메일: {self.email}, 주소: {self.addr}')
        #self.name 과 name 은 다른 존재.

    @staticmethod
    def set_contact():     # 정적 self없음 static #반 영속적으로 저장
        name = input('이름')
        phone = input('전화번호')
        email = input('이메일')
        addr = input('주소')
        contact = Contact(name, phone, email, addr) 
        # Contact는 클래스명
        # contact는 인스턴스명. 대소문자로 구분하는거 권장
        return contact

    @staticmethod
    def get_contact(clist):
        for i in clist:
            i.print_info() # print_info 에 선언된 메소드(클래스 내부에 선언된함수)
            # 함수는 클래스 밖에있음
    
    @staticmethod
    def del_contact(clist,name): # i 는 인덱스 t는 요소(인스턴스)출력
        for i,t in enumerate(clist):
            if t.name == name:
                del clist[i]

    @staticmethod
    def print_menu():
        print('1 연락처 입력')
        print('2 연락처 출력')
        print('3 연락처 삭제')
        print('4 종료')
        menu = input('메뉴선택: ')
        return menu

    @staticmethod
    def run():
        clist = []
        while 1:
            menu = Contact.print_menu()
            if menu =='1':
                t= Contact.set_contact()
                clist.append(t)
            
            if menu =='2':
                Contact.get_contact(clist) #static method 는 클래스가 직접 접근

            if menu =='3':
                name = input('삭제할 이름')
                Contact.del_contact(clist,name)

            if menu =='4':
                break

if __name__ == '__main__':
    Contact.run()
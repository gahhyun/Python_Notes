'''
        class 클래스 이름 :
            def __int__(self....):
                pass
            def 메서드1(self, ...):
                pass
'''

class Counter:
    def __init__(self, initVar=0):         #생성자
        self.count = initVar          # count : 인스턴스 변수
    def increament(self):       #메서드
        self.count += 1

a = Counter(0)       #기본 생성자 -> 객체가 만들어짐
print("카운터의 값 = " , a.count)
a.increament()
print("카운터의 값 = " , a.count)

b = Counter(100)
print("카운터의 값 = " , b.count)
b.increament()
print("카운터의 값 = " , b.count)


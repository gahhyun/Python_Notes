'''
    원을 클래스로 구현하시오
    클래스 이름은 Circle로 한다
        -생성자
        -반지름 (radius)
        -getArea()      :원의 넓이
        -getPrimeter()  : 원의 둘레

    출력예시  (반지름이 10인 원의 면적과 원의 둘레를 출력하시오)
        원의 면적 :
        원의 둘레 :
'''
import math

class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def getPrimeter(self):
        return  2 * self.radius * math.pi

    def getArea(self):
        return self.radius*self.radius*math.pi

c = Circle(10)
print("원의 면적 : ", c.getArea())
print("원의 둘레 : ", c.getPrimeter())



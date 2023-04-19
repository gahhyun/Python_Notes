class Student:
    def __init__(self, name=None, age=0):
        self.__name = name      #__가 변수 앞에 붙으면 외부에서 변경 불가(private)
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__Name

    def setAge(self):
        self.__age

    def setName(self):
        self.__Name


stu = Student("Admiral", 25)
print(stu.getName())
print(stu.setAge())
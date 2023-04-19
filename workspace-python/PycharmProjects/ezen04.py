'''
직각삼각형 판별하는 프로그램을 작성하시오

    변a의 길이 :
    변b의 길이 :
    변c의 길이 :
    직각삼각형입니다
'''

a = int(input('변a의 길이 :'))
b = int(input('변b의 길이 :'))
c = int(input('변c의 길이 :'))

if(a*a + b*b == c*c):
    print('직각삼각형입니다')
else:
    print('직각삼각형이 아닙니다')
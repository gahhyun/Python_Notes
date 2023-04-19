x=123
print(x)
print(type(x))

x=3.14
print(x)
print(type(x))

msg = 'hello'
print(msg)
print(type(msg))


# x = input('정수를 입력하세요: ')
# y = input('정수를 입력하세요: ')
# print(x+y)
#
# print()
# t = input('정수를 입력하세요: ')    #시용자가 입력한 데이터를 문자열 형태로 리턴
# y = int(t)
# print(y)
#
# t = input('정수를 입력하세요: ')
# y = int(t)
# print(y)
#
# print()
# x = float(input('실수를 입력하세요: '))
# y = float(input('실수를 입력하세요: '))
# print(x+y)

#문자열과 문자열만 연결가능함
#print('나는 현재'+28+'살 입니다') #오류

#정수를 문자열로 변환
print('나는 현재'+str(28)+'입니다')

#실수를 문자열로 변환
print('나는 현재'+str(28.5)+'입니다')

# * 연산자를 이용해서 반복시킬수 있음
print('='*30)

s = 'Hello python'
print(s[0])
print(s[1])
print(s[-1])
print(s[-12])

s = 'Hello world'
#인덱스 3까지의 접두사 가져오기
prefix = s[:4]
print(prefix)

#인데스 2부터 접미사 다 가져오기
x = s[2:]
print(x)

#중간에 있는 부분 문자열 가져오기
z = s[-4:-1]
q = s[7:10]
print(z)
print(q)




















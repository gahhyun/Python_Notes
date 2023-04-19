'''
score가 60이상이면  '합격입니다./ 수고하셨습니다'를 출력하는 프로그램을 작성하시오
'''

score = 90
if score >= 60:  # 마지막에 : 을 사용
    print("합격입니다.")    #반드시 들여쓰기 사용
    print('장학금 받습니다')
else:
    print('불합격입니다')
print('수고하셨습니다')

print('-'*30)

'''
    언어를 선택하세여(1.한국어 2.영어 3.프랑스 4.독일어)
    안녕
    언어를 선택하세여(1.한국어 2.영어 3.프랑스 4.독일어)
    bonjour
    언어를 선택하세여(1.한국어 2.영어 3.프랑스 4.독일어)
    Guten Morgen
'''

x = int(input("언어를 선택하세여(1.한국어 2.영어 3.프랑스 4.독일어)"))
if(x == 1):
    print('안녕')
if(x == 2):
    print('hello')
if(x == 3):
    print('bonjour')
if(x == 4):
    print('Guten Morgen')

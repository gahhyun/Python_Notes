import  numpy as np

print(np.zeros(3))      # 0이 3개 들어있는 배열 생성

print(np.zeros((2,2)))     # 요소의 값이 모두 0인 2 * 2 의 배열 생성

print(np.ones((3,2)))             #요소의 값이 모두 1인 3*2 의 배열 생성

a = np.array([-1,3,2,-6])
print(a)

b = np.array([3,6,1,2])
print(b, type(b))

A = np.reshape(a, [2,2])    # 배열a을 2행 2열로 변결
print(A)

B = np.reshape(b, [2,2])
print(B)                    # 배열b를 2행 2열로 변경
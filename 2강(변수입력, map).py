# a=input("숫자를 입력하세요 : ") #변수입력
# print(a)

a,b=input("숫자를 입력하세요 : ").split() #2 3 으로 입력한다면, split은 띄어쓰기 기준으로 변수를 각각 입력받게 해줌
print(a+b) # string 형으로 입력받았기 때문에 연산이 되진 않고, a와 b가 그냥 붙어져서 나옴
c = a+b
print(type(a))
print(type(b))
print(type(c))
print(c)

a = int(a) # int(a)는 정수형으로 바꿔줌
b = int(b)
print(type(a))
c = a+b
print(c)

a, b = map(int, input("숫자를 입력하세요 : ").split()) #map은 여러변수를 한번에 처리하게 끔 해줌
print(a+b)
print(a-b)
print(a*b)
print(a/b) #나누기 계산
print(a//b) #몫 구하는 것
print(a%b) #나머지 구하는 것
print(a**b) #거듭제곱 a^b 구하는 것

a = 4.3 #실수형
b = 5 #문자열
print(type(b))
c = a+b
print(type(c)) #더 큰 범위의 형태로 출력됨
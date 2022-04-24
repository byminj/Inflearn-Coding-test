a=1 #a 에 1을 삽입. a==1 은 a와 1은 같다.
A=2
A1=3
#2b = 4 앞에 # 붙이면 주석처리하는것
print(a,A,A1)

#값 교환
a, b = 10, 20
print(a,b)
a, b = b, a
print(a,b)

#변수 타입
a = 12345 #int:정수형
print(type(a))
print(a)
a=12.123456789123456789 #float:실수형 8바이트까지 저장됨. 그래서 .7까지 나옴, 뒤의 데이터는 손실된 것
print(type(a))
print(a)
a='student' #str:문자형
print(type(a))
print(a)

#출력방식
print("number")
a,b,c = 1,2,3
print(a,b,c)
print("number : ",a,b,c)
print(a,b,c, sep=', ') #각 변수 사이를 분리해줌. sep = separte
print(a,b,c, sep='\n') #\n은 줄 바꿈
print(a) #print는 기본으로 줄바꿈
print(b)
print(c)
print(a, end=' ') #print안에 end 넣으면 띄어쓰기 대신 붙여서 쓸 수 있음
print(b, end=' ')
print(c, end=' ')

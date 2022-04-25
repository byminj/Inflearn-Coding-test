'''
반복문을 이용한 문제풀이
 1) 1부터 N까지 홀수출력하기
 2) 1부터 N까지의 합 구하기
 3) N의 약수출력하기
'''

n=int(input()) #int를 넣어줘야 입력받은 숫자가 정수형이 됨
for i in range(1,n+1):
    if i%2==1:
        print(i)

n=int(input())
sum=0
for i in range(1,n+1):
    sum = sum+i
    print(sum) #이렇게 하면 for문 반복할때마다 출력함
print(sum) #여기에 두면 마지막 sum만 출력함

n = int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i, end=' ')

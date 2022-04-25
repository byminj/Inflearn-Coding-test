x=7
if x==7: #x가 7이 참이라면
    print("lucky") #lucky를 출력하라, *들여쓰기가 기준점임, 띄어쓰기 4개
    print("ㅋㅋ") #ㅋㅋ를 출력하라

if x!=7: #x가 7이 참이 아니라면
    print("lucky") #lucky를 출력하라

x=15
if x>=10: #x가 10 이상이면
    if x%2 == 1: #x가 홀수라면(나머지가 1인수)
        print("10이상의 홀수")

x = 9
if x>0:
    if x<10:
        print("10보다 작은 자연수")

x = 10
if x>0: #x가 0보다 크다면
    print("양수") #양수라 출력
else: #아니라면, 분기문 구조라 함
    print("음수") #음수라 출력

x = 93
if x>=90: #90이상이라면
    print("A")
elif x>=80: #elif는 위에서 참이라면 출력하고 끝냄. 참이 아닐때 아래로 쭉 내려옴
    print("B")
elif x>=70: #만약에 if라고 하면, 각각의 if문임. 따라서 참일 때마다 결과값을 출력함
    print("C")
elif x>=60:
    print("D")
else:
    print("F")

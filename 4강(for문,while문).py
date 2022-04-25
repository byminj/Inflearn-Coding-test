a=range(10) #0에서 9까지 순차적으로 정수를 만듦
print(list(a)) #range는 list형태로 출력해야함

a=range(1,11) #1부터 10까지 만듦
print(list(a))

for i in range(10): #0부터 9까지니까, 반복문이 10번 반복함. i가 0을 시작으로 9까지 10번 반복함
    print("hello")
    print(i)

for i in range(1,11):
    print(i)

for i in range(10,1,-1): # *숫자가 작아지는 것은 ,-step 을 입력해줘야함
    print(i)

i=1
while i<=10:
    print(i)
    i=i+1 #변수를 입력해줘야함. 안바꿔주면 i는 계속 1이니까, 무한반복함

i=10
while i>=1:
    print(i)
    i=i-1

i=1
while True: #참일 때 까지
    print(i)
    if i==10: #10이라면
        break #멈춤
    i+=1 #i=i+1

for i in range(1,11):
    if i%2==0: #짝수이면
        print(i) #출력

for i in range(1,11):
    if i%2==0: #짝수이면
        continue #continue 아래에 for문에 속해있는 것들을 스킵함. 따라서 짝수는 스킵되니까 홀수만 출력됨.
    print(i)

for i in range(1,11):
    print(i)
    if i==5:
        break #5가되면 break됨, 밑에 else도 하지 않음. 여기서 멈춤
else:
    print(11)

'''
문자열과 내장함수
'''

msg="It is Time"
print(msg.upper()) #대문자로 바꿔주는 함수 upper, msg함수를 대문자로 바꾸는 것은 아님
print(msg.lower())

tmp=msg.upper()
print(tmp)
print(tmp.find('T'))
'''
0 1 2 3 4 5 6 7 8 9
I T   I S   T I M E
find 는 이런식으로 찾아줌
'''
print(tmp.count(('T')))
print(msg)
print(msg[:2]) #[:2]는 0번부터 1번까지 추출하는 것
print(msg[3:5]) #3번 인덱스부터 5번까지
print(len(msg)) #공백도 문자임
for i in range(len(msg)): #여기서 len(msg)가 10이니까 0부터 9까지임
    print(msg[i], end='') #0부터 9까지 출력함
print() #줄바꾸는 용도로 썼음
for x in msg:
    print(x, end=' ')
print()
for x in msg:
    if x.isupper(): #x가 대문자라면,
        print(x, end=' ') #대문자만 출력됨
print()
for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): #공백 제외하고 문자만 출력함
        print(x, end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) #ord는 아스키 넘버를 출력함, A는 65, Z는90

tmp='az'
for x in tmp:
    print(ord(x)) #a는 97 z는 122

tmp=65
print(chr(tmp)) # 아스키코드 65에 대응하는 문자를 출력함


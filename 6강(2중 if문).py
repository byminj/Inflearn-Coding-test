'''
중첩 반복문(2중 for문)
'''
for i in range(5):
    for j in range(5): #i가 0일 때 j가 0부터 4까지 반복, i가 1일 때 ~~~
        print(j, end = ' ')
    print()

for i in range(5):
    print('i:', i, sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print() #줄바꿈 용도로 넣은 것

for i in range(5):
    for j in range(5):
        print("*", end=' ')
    print()

for i in range(5):
    for j in range(i+1): #i가 0일 때 range(1)이니까 1번 반복, i가 1일 때는 2번 반복 ~~~
        print("*", end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()

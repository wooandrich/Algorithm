number = int(input())
for i in range(number+1):
    print(i)

# 무한루프 while문을 세팅하는법

1. True 사용
while True:
    print(i)
    break
2. True == 1
while 1:
    print('a')
    break
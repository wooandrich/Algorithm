input = __import__('sys').stdin.readline
number = int(input())
for i in range(1,number+1):
    if i % 10 == 3:
        print('X',end=' ')
    elif i % 10 == 6:
        print('X',end=' ')
    elif i % 10 == 9:
        print('X',end=' ')
    else:
        print(i,end=' ')

input = __import__('sys').stdin.readline
A,B,C = map(int,input().split())
count = 0
money = C-B
if money <=0:
    print(-1)
else:
    print(A//money + 1)

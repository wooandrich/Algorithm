input = __import__('sys').stdin.readline #빠른입력
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(A+B)
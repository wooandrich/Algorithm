A = int(input())
B = int(input())
C = int(input()) # 입력
ans = str(A*B*C) # A,B,C를 곱하고 문자열로 변환
for i in range(10):
    print(ans.count(str(i))) # 0부터 9까지 몇번 나오는지 count를 이용하여 출력
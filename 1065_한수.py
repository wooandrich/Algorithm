ans = [] # 한수를 만들 리스트
n = int(input()) # 입력

for i in range(1,n+1): #입력값까지 반복문
    if i < 100: # 100미만일때는 무조건 한수이므로 리스트추가
        ans.append(i)
    else: # 100부터는 등차수열일때만 리스트추가
        if {(i // 10) % 10 - (i // 100)} == {(i % 10) - (i // 10) % 10}:
            ans.append(i)
print(len(ans)) # 리스트 갯수 출력
ans = [] #리스트생성
for i in range(9):
    ans.append(int(input())) # 정수값을 리스트에 입력
print(max(ans)) # 리스트 최댓값 출력
print(ans.index(max(ans))+1) #리스트 최댓값의 인덱스를 출력 1번째부터 시작하므로 +1
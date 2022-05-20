N = int(input())
number_list = list(map(int,input().split()))
max_number = max(number_list)
ans = 0
for i in range(N):
    ans += number_list[i] / max_number * 100
print(ans / N)

t = int(input())
for i in range(t):
    r, s = input().split()
    ans = ''
    for i in s:
        ans += int(r) * i
    print(ans)


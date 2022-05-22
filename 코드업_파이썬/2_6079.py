number = int(input())
ans = 1
i = 1
while 1:
    if ans >= number:
        print(i)
        break
    else:
        i += 1
        ans += i

n = int(input())
ans = 0

for i in range(n):
    s = input()
    error = 0
    for j in range(len(s)-1):
        if s[j] != s[j+1]:
            new_word = s[j+1:]
            if new_word.count(s[j]) > 0:
                error += 1
    if error == 0:
        ans += 1
print(ans)

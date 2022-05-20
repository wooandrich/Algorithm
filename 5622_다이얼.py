s = input()
ans = 0

for i in range(len(s)):
    if s[i] in 'A':
        ans += 3
    elif s[i] in 'B':
        ans += 3
    elif s[i] in 'C':
        ans += 3
    elif s[i] in 'D':
        ans += 4
    elif s[i] in 'E':
        ans += 4
    elif s[i] in 'F':
        ans += 4
    elif s[i] in 'G':
        ans += 5
    elif s[i] in 'H':
        ans += 5
    elif s[i] in 'I':
        ans += 5
    elif s[i] in 'J':
        ans += 6
    elif s[i] in 'K':
        ans += 6
    elif s[i] in 'L':
        ans += 6
    elif s[i] in 'M':
        ans += 7
    elif s[i] in 'N':
        ans += 7
    elif s[i] in 'O':
        ans += 7
    elif s[i] in 'P':
        ans += 8
    elif s[i] in 'Q':
        ans += 8
    elif s[i] in 'R':
        ans += 8
    elif s[i] in 'S':
        ans += 8
    elif s[i] in 'T':
        ans += 9
    elif s[i] in 'U':
        ans += 9
    elif s[i] in 'V':
        ans += 9
    elif s[i] in 'W':
        ans += 10
    elif s[i] in 'X':
        ans += 10
    elif s[i] in 'Y':
        ans += 10
    elif s[i] in 'Z':
        ans += 10
print(ans)
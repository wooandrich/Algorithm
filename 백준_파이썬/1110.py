N = int(input())
K = N
count = 0
while 1:
    a = int(N) // 10
    b = int(N) % 10
    c = a + b
    N = str(b) + str(c % 10)
    count += 1
    if int(N) == K:
        break
print(count)
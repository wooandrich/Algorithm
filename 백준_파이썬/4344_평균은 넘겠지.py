ans = 0
count = 0

c = int(input())

for i in range(c):
    case = list(map(int,input().split()))
    for j in range(case[0]):
        ans += case[j+1]
    a = ans / case[0]

    for k in range(case[0]):
        if case[k+1] > a:
            count += 1
    print('{:.3f}%'.format(count / case[0] * 100))
    ans = 0
    count = 0
    case = 0
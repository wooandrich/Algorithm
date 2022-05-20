ans = [] # 셀프넘버가 아닌 숫자로 이루어진 리스트
n = 1
def d(n): # 각 자리수 별 수열을 만드는 함수
    if n < 10:
        return n + n % 10
    elif n < 100:
        return n + n // 10 + n % 10
    elif n < 1000:
        return n + n // 100 + (n // 10) % 10 + n % 10
    elif n < 10000:
        return n + n // 1000 + (n // 100) % 10 + (n // 10) % 10 + n % 10

while 1:
    if n > 10000:
        break
    else:
        ans.append(d(n)) # 셀프넘버가 이닌 수들을 리스트에 추가
        n += 1

for i in range(1,10001):
    if i not in ans: # 반복문을 돌려 리스트에 없으면 i를 출력
        print(i)
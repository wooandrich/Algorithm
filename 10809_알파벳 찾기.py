s = input()
ans = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(alphabet)):
    if alphabet[i] in s:
        ans.append(s.index(alphabet[i]))
    else:
        ans.append(-1)
for j in ans:
    print(j,end=' ')
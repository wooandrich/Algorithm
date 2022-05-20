word = input().lower()
word_list = list(set(word)) # [b,a]
ans = []

for i in word_list: # i = b,a
    count = word.count(i)
    ans.append(count) # [1,3]
if ans.count(max(ans)) >= 2:
    print("?")
else:
    print(word_list[ans.index(max(ans))].upper())
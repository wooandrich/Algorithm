alphabet = ord(input())
a_number = ord('a')
for i in range(alphabet-a_number+1):
    print(chr(a_number+i),end=' ')
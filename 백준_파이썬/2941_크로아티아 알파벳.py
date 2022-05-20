input = __import__('sys').stdin.readline
alphabet = input()
t = 0
i = 0
while 1:
    if i == len(alphabet):
        break
    else:
        if alphabet[i] == 'c':
            if alphabet[i+1] == '=':
                i += 2
                t += 1
            elif alphabet[i+1] == '-':
                i += 2
                t += 1
            else:
                i += 1
                t += 1
        elif alphabet[i] == 'd':
            if alphabet[i+1] == 'z' and alphabet[i+2] == '=':
                i += 3
                t += 1
            elif alphabet[i+1] == '-':
                i += 2
                t += 1
            else:
                i += 1
                t += 1
        elif alphabet[i] == 'l':
            if alphabet[i+1] == 'j':
                i += 2
                t += 1
            else:
                i += 1
                t += 1
        elif alphabet[i] == 'n':
            if alphabet[i+1] == 'j':
                i += 2
                t += 1
            else:
                i += 1
                t += 1
        elif alphabet[i] == 's':
            if alphabet[i+1] == '=':
                i += 2
                t += 1
            else:
                i += 1
                t += 1
        elif alphabet[i] == 'z':
            if alphabet[i+1] == '=':
                i += 2
                t += 1
            else:
                i += 1
                t += 1
        else:
            i += 1
            t += 1
print(t-1)

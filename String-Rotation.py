def check(position , lenn):
    if position < 0:
        position = -position    
        if position > lenn:
            position = position % lenn
    else:
        if position > lenn:
            position = position % lenn
        position = -position
    return position

def change(word , c_posi):
    if word == '':
        return ''
    else:
        real = ''
        count = len(word)
        c_posi = check(c_posi , count)
        i = c_posi
        while True:
            if len(real) == len(n):
                break
            else:
                real += n[i]
            i += 1
            if i == len(n):
                i = 0
            else:
                continue
        return real



n = str(input())
c = int(input())

print(change(n , c))
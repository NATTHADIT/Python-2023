n = str(input())
c = len(n)
result = ''
p = 0
m = 1

if c % 2 == 1:
    for i in range(0,(c)):
        if i % 2 == 0:
            result += n[p]
            p += 1
        else:
            result += n[-m]
            m += 1
else:
    for i in range(0,c):
        if i != c or i != c - 1:
            if i % 2 == 0:
                result += n[p]
                p += 1
            else:
                result += n[-m]
                m += 1
        else:
            result += n[i]
print(result)
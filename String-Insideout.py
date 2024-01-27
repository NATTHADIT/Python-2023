n = str(input())

c = len(n)
a = int(c/2)

f = ''
s = ''
temp = ''

if c % 2 == 0:
    for i in range(0,c):
        if i <= (a - 1):
            f += n[i]
        else:
            s += n[i]
    result = f[::-1] + s[-1::-1]
    print(result)
else:
    for i in range(0,c):
        if i <= (a - 1):
            f += n[i]
        elif i == (a):
            temp = n[i]
        else:
            s += n[i]
    result = f[::-1] + temp + s[-1::-1]
    print(result)
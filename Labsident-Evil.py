n = int(input())
s = str(input())
s = s.split()
b = []
c = 0
result = ''
for i in s:
    temp = int(i)
    while temp > 0:
        temp -= n
        c += 1
    b.append(c)
print(c)

for i in range(0,len(b)):
    if i == len(b) - 1:
        result += str(b[i])
    else:
        result += str(b[i])
        result += ' '
print(result)
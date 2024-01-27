a = []
suma = []

while True:
    s = int(input())
    if s == 0:
        break
    else:
        a.append(s)
for i in range(0,len(a) - 1):
    for j in range(1,len(a) + 1):
        temp = a[i:j]
        if len(temp) != 0:
            suma.append(sum(temp))
print(max(suma))
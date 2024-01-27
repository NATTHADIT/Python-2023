n = str(input())
listo = []
i = 0
n = n.lower()
while i < len(n) - 1:
    re = ''
    re += n[i]
    re += n[i + 1]
    if re not in listo:
        listo.append(re)
    i += 1
listo.sort()
for i in listo:
    print(i)
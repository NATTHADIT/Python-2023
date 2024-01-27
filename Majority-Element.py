n = int(input())
ls = []
major = {}
can = n/2
result = []
i = 0
while i < n:
    s = str(input())
    ls.append(s)
    i += 1
for i in ls:
    if i not in major:
        major[i] = 1
    else:
        major[i] += 1

for i in major:
    if major[i] > can:
        result.append(i)
    else:
        continue
if result == []:
    print(0)
else:
    for i in result:
        print(i)
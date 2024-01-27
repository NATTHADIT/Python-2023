n = int(input())
num = []
templist = []
i = 0
minn = 999999
result = []
while i < n:
    s = int(input())
    if s > 0:
        if s not in num:
            num.append(s)
    i += 1
num.sort()
for i in range(0,len(num) - 1):
    for j in range(i+1,i+2):
        temp = num[i:j+1]
        templist.append(temp)
for i in templist:
    if i[1] - i[0] < minn:
        minn = i[1] - i[0]
    else:
        continue

for i in templist:
    if i[1] - i[0] == minn:
        result.append(i)

for i in result:
    print(f"{i[0]} {i[1]}")
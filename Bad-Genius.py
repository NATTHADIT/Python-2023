s = str(input())
temp = ''
tempdict = {}
result = ''
s = s.split()
for i in s:
    for ch in i :
        if ch not in temp:
            temp += ch

n = str(input())

for i in range(0,len(n)):
    tempdict[n[i]] = temp[i]

dkey = tempdict.keys()

r = str(input())
for i in r:
    if i in dkey:
        result += tempdict.get(i)
    else:
        result += i

print(result)
n = str(input())
n = n.lower()
i = 0
count = 0
while i < len(n):
    if i == 0:
        count += 1
        i += 1
        continue
    else:
        if ord(n[i]) > ord(n[i - 1]):
            count += 1
            i += 1
        else:
            if i < 1:
                i += 1
                continue
            else:
                break
print(count)
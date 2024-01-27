def find(n):
    maxx = 0
    p = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for i in n:
        for j in range(13):
            if i == p[j] and j > maxx:
                maxx = j
    return p[maxx]
    
    
n = str(input())
i = 0

alllist = []
final = []
use = []
alllist.append(n)
for li in alllist:
    li = li.split()
    result = 0
    for card in li:
        if result <= 16:
            if card not in "23456789":
                if card == "A":
                    result += 1
                    use.append(card)
                    continue
                else:
                    use.append(card)
                    result += 10
                    continue
            else:
                result += int(card)
                use.append(card)
    if result > 21:
        final.append("busted")
    else:
        final.append(result)
print(find(use))
for i in final:
    print(i)
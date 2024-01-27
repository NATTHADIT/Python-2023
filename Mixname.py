f = str(input())
s = str(input())
vowel = ['a','e','i','o','u']
result = ''

count1 = 0
for ch in f:
    if ch in vowel:
        count1 += 1
    if count1 < 2:
        result += ch

count2 = 0
for ch in s:
    if ch in vowel and count2 < 1:
        count2 += 1
        continue
    if count2 >= 1:
        result += ch
if count2 == 0:
    result += s
        
print(result)
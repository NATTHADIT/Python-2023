n = str(input())
s = int(input())
n = n.split(',')
n.pop()
print(n[(s%7) - 1])
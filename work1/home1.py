mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
a = [int(x) for x in input().split()]
k = set(a)
b = [int(x) for x in input().split()]
k1 = set(b)
spisok = []
for el in k:
    if el in k1:
        spisok.append(el)
print(spisok)
n = int(input("1 - ая доля: "))
m = int(input("2 - ая доля: "))
k = int(input("количество чтобы отломить: "))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')
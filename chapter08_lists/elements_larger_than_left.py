# 1 3 7 2 5 9 0 12

l1 = [int(n) for n in input().split()]
print(l1)
for i in range(1, len(l1)):
    if l1[i] > l1[i - 1]:
        print(l1[i])

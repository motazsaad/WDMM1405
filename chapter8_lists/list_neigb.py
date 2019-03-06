def same_sign(x, y, z):
    if x > 0 and y > 0 and z > 0:
        return True
    elif x < 0 and y < 0 and z < 0:
        return True
    else:
        return False


l1 = [int(n) for n in input().split()]
print(l1)
# l1 = '1 5 2 4 3'.split()
# 5 4

# for i in range(1, len(l1)):
#     if l1[i] > l1[i-1]:
#         print(l1[i])

for i in range(1, len(l1) - 1):
    if same_sign(l1[i - 1], l1[i], l1[i + 1]):
        print(l1[i])

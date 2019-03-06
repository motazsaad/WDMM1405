'''
write a program to print numbers that has the
same sign with their left and right neighbors
'''


def is_same_sign(x, y, z):
    if x >= 0 and y >= 0 and z >= 0:  # all positive
        return True
    elif x < 0 and y < 0 and z < 0:  # all negative
        return True
    else:
        return False  # some are positive and some are negative


l1 = [int(n) for n in input().split()]
print(l1)
for i in range(1, len(l1) - 1):
    if is_same_sign(l1[i - 1], l1[i], l1[i + 1]):
        print(l1[i])

def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False


def is_odd(num):
    if (num % 2) == 0:
        return False
    else:
        return True


l1 = [1, 3, 2, 5, 7, 12]
for i in range(len(l1)):
    if is_even(i):
        print(l1[i])
print('----------------')
for n in l1:
    if is_even(n):
        print(n)

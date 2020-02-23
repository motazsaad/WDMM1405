def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


# even indices
# even elements
l1 = [int(n) for n in input().split()]
print(l1)

print('even indices:')
for i in range(len(l1)):
    if is_even(i):
        print(l1[i])

print('---------------')
print('even elements')
for n in l1:
    if is_even(n):
        print(n)

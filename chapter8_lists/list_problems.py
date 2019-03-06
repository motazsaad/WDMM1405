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


print('even test')
for i in range(11):
    print(i, 'is even?', is_even(i))

print('odd test')
for i in range(11):
    print(i, 'is odd?', is_odd(i))

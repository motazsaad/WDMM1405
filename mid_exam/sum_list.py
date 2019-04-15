def sum_lists(a, b):
    if len(a) != len(b):
        return -1
    else:
        return [x + y for x, y in zip(a, b)]


print(sum_lists([1, 3, 4], [4, 5, 6]))
print(sum_lists([5, -5, 12], [3, 5]))

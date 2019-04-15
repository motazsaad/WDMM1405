def get_neighbors(a):
    result = []
    for i in range(1, len(a) - 1):
        if a[i - 1] == a[i + 1]:
            result.append(a[i])
    return result


print(get_neighbors([1, 2, 1, 2, 4, 4, 3]))
print(get_neighbors([1, 2, 1, 2, 4, 4, 4]))

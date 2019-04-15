def get_top_std(students):
    max_score = max(students.values())
    top_std = []
    for std_id in students.keys():
        if students[std_id] == max_score:
            top_std.append(std_id)
    return top_std


print(get_top_std({'120191122': 90,
                   '120172233': 87,
                   '120103344': 90,
                   '120091122': 93}))

print(get_top_std({'120161234': 60,
                   '120172233': 89,
                   '120103344': 89,
                   '120001999': 78}))


def sum_lists(a, b):
    if len(a) != len(b):
        return -1
    else:
        return [x + y for x, y in zip(a, b)]


print(sum_lists([1, 3, 4], [4, 5, 6]))
print(sum_lists([5, -5, 12], [3, 5]))


def most_freq_word(text, n):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return sorted([(v, k) for k, v in counts.items()], reverse=True)[:n]


print(most_freq_word('''the clown ran
after the car and
the car ran into the tent and the tent
fell down on the
clown and the car''', 5))


def get_neighbors(a):
    result = []
    for i in range(1, len(a) - 1):
        if a[i - 1] == a[i + 1]:
            result.append(a[i])
    return result


print(get_neighbors([1, 2, 1, 2, 4, 4, 3]))
print(get_neighbors([1, 2, 1, 2, 4, 2, 3]))

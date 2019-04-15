def get_top_std(students):
    # step 1 : get the max mark
    max_score = max(students.values())
    # step 2: get std id with max_score
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

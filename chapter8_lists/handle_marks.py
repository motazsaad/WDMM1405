def get_count(mark_list, m):
    count = 0
    for mark in mark_list:
        if mark >= m:
            count += 1
    return count


infile = open('marks.csv', encoding='utf-8')
marks = []
for line in infile:
    if line.startswith('#'):
        continue
    numbers_str = line.strip().split('\t')
    # print(numbers_str)
    numbers_int = [int(n) for n in numbers_str]
    # print(numbers_int)
    # print('mark:', sum(numbers_int))
    marks.append(sum(numbers_int))

print('average', sum(marks) / len(marks))
print('success count', get_count(marks, 60))
marks = [m + 8 for m in marks]
print('after push')
print('average', sum(marks) / len(marks))
print('success count', get_count(marks, 60))
outfile = open('marks_after_push.txt', mode='w')
outfile.write('\n'.join([str(m) for m in marks]))
infile.close()
outfile.close()

outfile = open('marks_after_push.txt', mode='a')
outfile.write('\naverage: {}'.format(sum(marks) / len(marks)))
outfile.close()

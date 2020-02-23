def get_count(mark_list, m):
    count = 0
    for mark in mark_list:
        if mark >= m:
            count += 1
    return count


infile = open('marks.csv', encoding='utf-8')
marks = []
outfile = open('marks_with_total.csv', mode='w')
outfile.write('#mid\tlab\tfinal\ttotal\n')
for line in infile:
    if line.startswith('#'):
        continue
    numbers_str = line.strip().split('\t')
    # print(numbers_str)
    numbers_int = [int(n) for n in numbers_str]
    # print(numbers_int)
    # print('mark:', sum(numbers_int))
    total = sum(numbers_int)
    marks.append(total)
    outfile.write('{}\t{}\t{}\t{}\n'.format(numbers_int[0], numbers_int[1], numbers_int[2], total))

infile.close()
outfile.close()

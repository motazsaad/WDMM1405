'''
you have a file with 3 columns (mid, lab, final)
write a program to create a file with the 3 columns
and with a fourth column (total)
add the average for each column
'''


def avg(alist):
    return sum(alist) / len(alist)


infile = open('marks.csv', encoding='utf-8')
marks = []  # total
mid = []
final = []
lab = []
outfile = open('marks_with_total_and_avg.csv', mode='w')
# write header
outfile.write('#mid,lab,final,total\n')
for line in infile:
    if line.startswith('#'):
        continue
    numbers_str = line.strip().split('\t')
    numbers_int = [int(num) for num in numbers_str]
    total = sum(numbers_int)
    marks.append(total)
    mid.append(numbers_int[0])
    lab.append(numbers_int[1])
    final.append(numbers_int[2])
    outfile.write('{},{},{},{}\n'.format(numbers_int[0], numbers_int[1], numbers_int[2], total))

outfile.write('{},{},{},{}\n'.format(avg(mid), avg(lab), avg(final), avg(marks)))

infile.close()
outfile.close()

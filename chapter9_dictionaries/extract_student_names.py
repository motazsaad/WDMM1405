file_name = 'C:\\Users\\Motaz Saad\\Documents\\MEGAsync\\التدريس\\مساقات حالية\\بايثون 2\\students-names\\std_names.csv'
infile = open(file_name, encoding='utf-8')
outfile1 = open('male_students.txt', encoding='utf-8', mode='w')
outfile2 = open('female_students.txt', encoding='utf-8', mode='w')
for line in infile:
    if line.strip().startswith('#'):
        continue
    tokens = line.replace('\"', '').split(',')
    name = tokens[0]
    first_name = name.split()[0]
    std_id = tokens[3]
    if std_id.startswith('1'):
        outfile1.write(first_name + '\n')
    elif std_id.startswith('2'):
        outfile2.write(first_name + '\n')

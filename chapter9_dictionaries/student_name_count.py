# infile = open('female_students.txt', encoding='utf-8')
infile = open('male_students.txt', encoding='utf-8')
name_dict = {}
names = infile.read().split('\n')
for name in names:
    name_dict[name] = name_dict.get(name, 0) + 1

for k, v in name_dict.items():
    print(k, v)

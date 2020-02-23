infile = open('text.txt')
outfile = open('processed.txt', mode='w')
for line in infile:
    new_line = ''  # empty string
    for word in line.split():
        if word.islower():
            new_line += word.upper() + ' '
        elif word.isupper():
            new_line += word.lower() + ' '
        else:
            new_line += word + ' '
    outfile.write(new_line + '\n')
outfile.close()
infile.close()

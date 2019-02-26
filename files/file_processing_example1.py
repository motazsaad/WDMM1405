infile = open('text.txt')
outfile = open('processed2.txt', mode='w')
for line in infile:
    for word in line.split():
        if word.islower():
            outfile.write(word.upper() + ' ')
        elif word.isupper():
            outfile.write(word.lower() + ' ')
        else:
            outfile.write(word + ' ')
    outfile.write('\n')
outfile.close()
infile.close()

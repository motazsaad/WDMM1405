infile = open('mbox.txt')
outfile = open('emails_2007_102.txt', mode='w')
count = 0
for line in infile:
    clean_line = line.strip()
    if clean_line.startswith('From') and clean_line.endswith('2007'):
        p1 = clean_line.find(' ')
        p2 = clean_line.find(' ', p1 + 1)
        email = clean_line[p1 + 1:p2]
        outfile.write(email + '\n')
        count += 1
print('email count', count)
infile.close()
outfile.close()

outfile = open('emails_2007_102.txt', mode='a')
outfile.write('\nemail count ' + str(count))

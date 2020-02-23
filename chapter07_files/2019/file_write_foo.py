infile = open('mbox.txt')
outfile = open('sent_emails_2007.txt', mode='w')
for line in infile:
    clean_line = line.strip()
    if clean_line.startswith('From') and clean_line.endswith('2007'):
        p1 = clean_line.find(' ')
        p2 = clean_line.find(' ', p1 + 1)
        email = clean_line[p1 + 1:p2]
        outfile.write(email + '\n')
outfile.close()

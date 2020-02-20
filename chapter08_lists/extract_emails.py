infile = open('../files/mbox.txt')
outfile = open('emails.txt', mode='w')
for line in infile:
    clean_line = line.strip()
    if clean_line.startswith('From '):
        tokens = clean_line.split()
        email = tokens[1]
        year = tokens[-1]
        domain = email.split('@')[1]
        outfile.write('domain: {}\tyear: {}\n'.format(domain, year))
infile.close()
outfile.close()

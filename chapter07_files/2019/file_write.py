outfile = open('my-file.txt', mode='w', encoding='utf-8')
outfile.write('hello world')
outfile.write('\nhello again')
outfile.close()

# overwrite 
outfile2 = open('my-file-2.txt', mode='w', encoding='utf-8')
outfile2.write('مرحبا')
outfile2.write('\nالسلام عليكم ')

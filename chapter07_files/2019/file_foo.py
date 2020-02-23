infile1 = open('text.txt', mode='r', encoding='utf-8')
for line in infile1:
    print(line.strip())
infile1.close()
print('-----------------')
infile2 = open('my-file.txt')  # default is read mode
text = infile2.read()
print(text)

# method 1: read line by line
file_handle = open('Ahmed_file.txt')
for line in file_handle:
    print(line.strip())
# method 2: read the whole file
file_handle = open('Ahmed_file.txt')
text = file_handle.read()
print(text)
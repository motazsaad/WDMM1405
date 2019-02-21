file_handle = open('text.txt', 'r')
#print(file_handle)
# way 1 to read the file
print('way 1')
for line in file_handle:
    print(line.strip())
file_handle.close()
# way 2 to read the file
file_handle = open('text.txt', 'r')
print('way 2')
text = file_handle.read() # read the whole file
print(text)
file_handle.close()
file_name = input('enter file name: ')
try:
    infile = open(file_name, mode='r')
    text = infile.read()
    print(text)
except FileNotFoundError:
    print('file not found')

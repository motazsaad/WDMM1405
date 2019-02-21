# break & continue
while True:
    my_input = input('what is your name? ')
    if my_input.startswith('#'):
        continue  # go to line 2
    if my_input == 'exit' or my_input == 'quit':
        break  # go to line 9
    print('welcome ' + my_input)
print('done')

# none deterministic loop
ans = 'yes'
while ans == 'yes':
    my_input = input('what is your name? ')
    print('welcome ' + my_input)
    ans = input('again? yes/no ')
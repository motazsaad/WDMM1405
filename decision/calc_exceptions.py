try:
    num1 = int(input('enter 1st number: '))
    op = input('enter operator: ').strip()
    num2 = int(input('enter 2nd number: '))
    if op is '+':
        print(num1 + num2)
    elif op is '-':
        print(num1 - num2)
    elif op is '*':
        print(num1 * num2)
    elif op is '/':
        print(num1 / num2)
except ValueError:
    print('input must be numeric')
except ZeroDivisionError:
    print('can not divide by zero')

try:
    num1 = float(input('enter 1st number: '))
    op = input('enter operator: ').strip()
    num2 = float(input('enter 2nd number: '))
    if op is '+':
        print(num1 + num2)
    elif op is '-':
        print(num1 - num2)
    elif op is '*':
        print(num1 * num2)
    elif op is '/':
        print(num1 / num2)
except ValueError:
    print('error: input must be numeric')
except ZeroDivisionError:
    print('error: can not divide by zero')

x = 10  # statement
x = 10  # assignment
y = x + 3  # expression and assignment
print(2 ** 3)  # power: 2*2*2
print(divmod(23, 5))  # (4, 3)
print(23 // 5)  # 4
print(23 % 5)  # 3
# types: int, float, str
x = 10
print(type(x))  # <class 'int'>
x = 10.1
print(type(x))  # <class 'float'>
x = 'abc'
print(type(x))  # <class 'str'>
print(10 / 3)  # float result
print(10 / 2)  # float result

print('abc' + '123')  # concat
# print('abc' - 'qwerty') Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

print(str(123))
print(str(12.3))
print(int('133'))
# print(int('133abc'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '133abc'
# print(int('13.3'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '13.3'
print(float('13.3'))
# print(float('13.3.1'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: could not convert string to float: '13.3.1'

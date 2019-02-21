# re-implement some Python built-in functions


def my_max(l1):
    max_number = l1[0]
    for number in l1:
        if number > max_number:
            max_number = number
    return max_number


def my_sum(l1):
    total = 0
    for number in l1:
        total += number
    return total


def my_len(l1):
    count = 0
    for i in l1:
        count += 1
    return count


def my_divmod(x, y):
    result = x // y
    reminder = x % y
    return result, reminder


def my_power(x, y):
    return x ** y

# use loops for:
# find number
# operation (sum, average, sum with condition, count)

number = 3
new_value = 13
l1 = [1,3,4,7,3, 9, 3]
print('before', l1)
for i in range(len(l1)):
    if l1[i] == number:
        l1[i] = new_value
print('after', l1)
print('before', l1)
for i in range(len(l1)):
    if l1[i] > 5:
        l1[i] += 2
print('after', l1)
print('before sum', l1)
total = 0
for n in l1: # no need for index
    total += n
print('after sum', l1)

key = int(input('enter a number: '))
for i in range(len(l1)):
    if l1[i] == key:
        print(i)
        break


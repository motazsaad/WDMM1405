# for range
# for iteration var in list

l1 = [1,3,4,7,3, 9, 3]


# change all 3s to 13
print('before', l1)
for i in range(len(l1)):
    if l1[i] == 3:
        l1[i] = 13
print('after', l1)


# if the value > 5, then add 2
print('before', l1)
for i in range(len(l1)):
    if l1[i] > 5:
        l1[i] += 2
print('after', l1)


# find the position of 7 in the list
for i in range(len(l1)):
    if l1[i] == 7:
        print(i)


# find the average
total = 0
count = 0
for n in l1: # iteration variable, no need for the index
    total += n
    count += 1
print('average', total/count)
print(l1)
key = int(input('enter a number: '))
for i in range(len(l1)):
    if l1[i] == key:
        print(i)
        break


# find the max value
print(l1)
max = l1[0]
for i in range(len(l1)):
    if l1[i] > max:
        max = l1[i]
print(max)
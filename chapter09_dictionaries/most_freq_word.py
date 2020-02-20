'''
write a program to find the most frequent word in
a text entered by the user
'''

counts = dict()
counts.se
print('Enter a line of text:')
line = input('')

print('Counting...')
for word in line.split():
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

max_v = 0
for k, v in counts.items():
    if v > max_v:
        max_v = v
        most_freq_word = k

print('most frequent word:', most_freq_word)
print('the frequency of most frequent word:', max_v)

def most_freq_word(text, n):
    counts = {}
    # step 1: count
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    # step 2: get n most freq words
    # key = word: value: freq
    return sorted([(v, k) for k, v in counts.items()], reverse=True)[:n]


print(most_freq_word('''the clown ran
after the car and
the car ran into the tent and the tent
fell down on the
clown and the car''', 3))

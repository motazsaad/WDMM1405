'''
Write a program to count the number of words that start with a consonant
and end with a vowel in a string. Example of such words: (life, gateau, pizza).
You must write a function determine if a word starts with a consonant
and ends with a vowel, then use this function in your code.
'''

text = """LOW FAT MOHALLABIAH RECIPE
In a casserole, bring to boil fat-free sweetened Condensed Milk with 4 cups of water. 
In another bowl, dissolve the remaining water with the rice powder and vanilla powder.
Slowly pour the rice mixture over the hot milk constantly stirring and cook on low heat 
for 5 minutes or until the mixture thickens. Add the rose and blossom water and mix well.
Pour the mixture into small bowls, and garnish with the grated pistachio.
"""


def check_word(word):
    vowels = 'aeiouAEIOU'
    if word[0] not in vowels and word[-1] in vowels:
        return True
    else:
        return False


count = 0
for w in text.split():
    if check_word(w):
        count += 1
        print(w)

print(count)

import random as r


word_list = ['apples','oranges','bananas','mangoes', 'strawberries']
word = r.choice(word_list)
print(word)

print('Please enter a single letter;')
guess = input()

if len(guess) == 1 & guess.isalpha()==True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
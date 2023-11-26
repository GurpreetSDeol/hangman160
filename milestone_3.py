import random as r


word_list = ['apples','oranges','bananas','mangoes', 'strawberries']
word = r.choice(word_list)

while True:
    
    print('Please enter a single letter;')
    guess = input()

    if len(guess) == 1 & guess.isalpha()==True:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
        
if guess in word:
    print('Good guess!'+" "+ guess+" "+ 'is in the word')
else: 
    print('Sorry,'+" "+ guess+" "+ 'is not in the word. Try again')
    
    
def check_guess(guess):
    guess.lower()
    if guess in word:
      print('Good guess!'+" "+ guess+" "+ 'is in the word')
    else: 
      print('Sorry,'+" "+ guess+" "+ 'is not in the word. Try again')
      
def ask_for_input():
    while True:
        
        print('Please enter a single letter;')
        guess = input()

        if len(guess) == 1 & guess.isalpha()==True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()
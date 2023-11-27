import random as r

class Hangman:
    
    def __init__(self, word_list,num_lives = 5):
        
        self.word_list=word_list
        self.num_lives = 5
        self.word = self.choose_word()
        self.word_guessed = self.fill_empty_list()
        self.num_letters = self.get_unique_letters() 
        self.list_of_guesses = []
        
        def choose_word(self):
            return r.choice(self.word_list)
   
        def fill_empty_list(self):
            return ["_"] * len(self.word)
   
        def get_unique_letters(self):
           return len(set(self.word))
        
        def check_guess(self, guess):
            guess = guess.lower()
          
            if guess in self.word:
              print('Good guess!'+" "+ guess+" "+ 'is in the word')
              for i in range(0,len(self.word)):
                 if self.word[i]==guess:
                     self.word_guessed[i]=guess
              self.num_letters -=1
          
            else: 
              self.num_lives-=1
              print('Sorry,'+" "+ guess+" "+ 'is not in the word')
              print('You have'+" "+ self.num_lives +" "+ 'lives left')
              
        def ask_for_input(self):
            while True:
                
                print('Please enter a single letter;')
                guess = input()

                if not len(guess) != 1 & guess.isalpha()==True:
                    print('Invalid letter. Please, enter a single alphabetical character.')
                    
                elif guess in self.list_of_guesses:
                    print('You already tried that letter')
                    
                else:
                  check_guess(guess)
                  self.list_of_guesses.append(guess)
    
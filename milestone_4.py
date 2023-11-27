import random as r

class Hangman:
    
    def __init__(self, word_list,num_lives = 5):
        
        self.word_list=word_list
        self.num_lives = 5
        self.word = r.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        

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
          
          '''
          This function asks the user for a single alphabetical input
          
          
          '''
             
          
          while True:
                  
                  print('Please enter a single letter;')
                  guess = input()

                  if len(guess) != 1 & guess.isalpha()!=True:
                      print('Invalid letter. Please, enter a single alphabetical character.')
                      break
                      
                  elif guess in self.list_of_guesses:
                      print('You already tried that letter')
                      break
                      
                  else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    break
    
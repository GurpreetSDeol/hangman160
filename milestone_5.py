import random as r

class Hangman:
    
    '''
    This class is used for tbe Hangman game

    Attributes:
        word_list: list of words to choose from at random
        num_lives: the number of guesses the user gets
    '''
    
    def __init__(self, word_list,num_lives = 5):
        
        self.word_list=word_list
        self.num_lives = 5
        self.word = r.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        

        
    def check_guess(self, guess):
            guess = guess.lower()
            
            '''
            This function checks if the user guessed letter is in the word
            
            args:
                guess (str)
            '''
          
            if guess in self.word:
              print('Good guess!'+" "+ guess+" "+ 'is in the word')
              for i in range(0,len(self.word)):
                 if self.word[i]==guess:
                     self.word_guessed[i]=guess
              self.num_letters -=1
          
            else: 
              self.num_lives-=1
              print('Sorry,'+" "+ guess+" "+ 'is not in the word')
              print(f"You have {self.num_lives} lives left")
        
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



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
       
        if game.num_lives==0:
            print('You lost!')
            break
        elif game.num_letters>0:
            game.ask_for_input()
            
        elif game.num_lives > 0 & game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        
            
        
            
    
word_list = ['apples','oranges','bananas','mangoes']
play_game(word_list)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
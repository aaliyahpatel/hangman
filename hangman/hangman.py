import random







class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.word_guessed = list("_" * len(self.word))
        self.logos = [''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''' , '''
                               _       _ 
                              (_)     | |
  _   _  ___  _   _  __      ___ _ __ | |
 | | | |/ _ \| | | | \ \ /\ / / | '_ \| |
 | |_| | (_) | |_| |  \ V  V /| | | | |_|
  \__, |\___/ \__,_|   \_/\_/ |_|_| |_(_)
   __/ |                                 
  |___/                                  ''' , '''
                      _                _ 
                     | |              | |
  _   _  ___  _   _  | | ___  ___  ___| |
 | | | |/ _ \| | | | | |/ _ \/ __|/ _ \ |
 | |_| | (_) | |_| | | | (_) \__ \  __/_|
  \__, |\___/ \__,_| |_|\___/|___/\___(_)
   __/ |                                 
  |___/                                  ''']
        self.list_images = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

        print(self.logos[0])
        print("Welcome to Hangman!")

    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print (f"Good guess! {guess} is in the word.")
            self.num_letters -= 1
            for position in range(len(self.word)):
                letter = self.word[position]
                if letter == guess:
                    self.word_guessed[position] = letter
        
        
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        
        self.list_of_guesses.append(guess)
        print(f"{' '.join(self.word_guessed)}")
        

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                self.check_guess(guess)
                break


def play_game():
    word_list = ["strawberry", "pineapple", "passionfruit", "apple", "orange"]
    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print(f"You have no more lives left. The word was {game.word}")
            print(game.logos[2])
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(game.logos[1])
            break
        print (game.list_images[game.num_lives])



play_game()






            
            







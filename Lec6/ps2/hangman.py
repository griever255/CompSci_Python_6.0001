# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    guessed = True
    for i in range(len(secret_word)):
      if secret_word[i] not in letters_guessed:
        guessed *= False
    return guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    guessed_word = []
    for i in range(len(secret_word)):
      if secret_word[i] in letters_guessed:
        guessed_word.append(secret_word[i])
      else:
        guessed_word.append("_ ")
    return "".join(guessed_word)      



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    available_letters = []
    for letter in alphabet:
        if letter not in letters_guessed:
          available_letters.append(letter)
    return "".join(available_letters)


def unique_letters(secret_word):
  """
  secret_word: string, the secret word to guess
  returns: integer number of unique letters in the secret word
  """
  unique_letters = []
  for letter in secret_word:
    if letter not in unique_letters:
      unique_letters.append(letter)
  return len(unique_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    def Initialize():
      """Welcomes and displays the length of the secret word
      """
      total_letters = len(secret_word)
      print(f"Welcome to Hangman!\nI am thinking of a word that is {total_letters} letters long.")
    
    def guess_a_letter():
      """Asks the user for an input string. Returns the string
      """
      print(f"-----------------\nYou have {warnings} warnings left.\nYou have {guesses} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}")
      guess = input("Please guess a letter: ")
      return guess

    def isGood(guess):
        """Returns a boolean tuple of (True = guess is valid, True = guess was guessed before)
        """
        if guess and guess.lower() in get_available_letters(letters_guessed):
          letters_guessed.append(guess.lower())
          return True, False
        else:
          if guess.isalpha():
            return False, True
          else:
            return False, False
    
    def give_warning(isDuplicate):
      if warnings == 1:
        plural = "warning"
      else:
        plural = "warnings"
      if isDuplicate:  
          print(f"Oops! That was already guessed. You have {warnings} {plural} left: {get_guessed_word(secret_word, letters_guessed)}")  
      else:
          print(f"Oops! That is not a valid input. You have {warnings} {plural} left: {get_guessed_word(secret_word, letters_guessed)}")  

    guesses = 6
    warnings = 3
    letters_guessed = []
    Initialize()
    vowels = ["a","e","i","o","u"]

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
      guess = guess_a_letter()
      valid = isGood(guess)[0]
      duplicate = isGood(guess)[1]
      if valid:
        if guess.lower() in secret_word:
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
          if guess in vowels:
            guesses -= 2
          else:
            guesses -= 1
      else: 
        warnings -= 1
        if warnings == 0:
          print(f"Oops! That is not a valid input. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
          guesses -= 1
          warnings = 3
        else:
          give_warning(duplicate)
      
    if is_word_guessed(secret_word, letters_guessed):
      score = guesses*unique_letters(secret_word)
      print(f"Congratulations, you won!\nYour total score for this game is: {score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
    corresponding letters of other_word, or the letter is the special symbol
    _ , and my_word and other_word are of the same length;
    False otherwise: 
    '''
    match = True
    guessed_word = my_word.replace(" ","") # Remove spaces
    if len(guessed_word) == len(other_word): # Test to see if they're the same length
      for c in range(len(guessed_word)): # For each letter in guessed word
        if guessed_word[c] == other_word[c]: 
            pass # If the letters match, do nothing
        elif guessed_word[c] == "_": # If the letter is blank
          if other_word[c] in guessed_word: # Check to make sure it wasn't guessed
            match = False # If it was guessed, return False
        else:
            match = False # If the letters don't match, return False
    else:
       match = False # Ff they're not the same length, return False
    return match


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""
    for word in wordlist:
      if match_with_gaps(my_word, word):
        possible_matches += " " + word
    print(possible_matches.strip())
    

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    def Initialize():
      """Welcomes and displays the length of the secret word
      """
      total_letters = len(secret_word)
      print(f"Welcome to Hangman!\nI am thinking of a word that is {total_letters} letters long.")
    
    def guess_a_letter():
      """Asks the user for an input string. Returns the string
      """
      print(f"-----------------\nYou have {warnings} warnings left.\nYou have {guesses} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}")
      guess = input("Please guess a letter: ")
      return guess

    def isGood(guess):
        """Returns a boolean tuple of (True = guess is valid, True = guess was guessed before)
        """
        if guess and guess.lower() in get_available_letters(letters_guessed):
          letters_guessed.append(guess.lower())
          return True, False
        else:
          if guess.isalpha():
            return False, True
          else:
            return False, False
    
    def give_warning(isDuplicate):
      if warnings == 1:
        plural = "warning"
      else:
        plural = "warnings"
      if isDuplicate:  
          print(f"Oops! That was already guessed. You have {warnings} {plural} left: {get_guessed_word(secret_word, letters_guessed)}")  
      else:
          print(f"Oops! That is not a valid input. You have {warnings} {plural} left: {get_guessed_word(secret_word, letters_guessed)}")  

    guesses = 6
    warnings = 3
    letters_guessed = []
    Initialize()
    vowels = ["a","e","i","o","u"]

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
      guess = guess_a_letter()
      valid = isGood(guess)[0]
      duplicate = isGood(guess)[1]
      if valid:
        if guess.lower() in secret_word:
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
          if guess in vowels:
            guesses -= 2
          else:
            guesses -= 1
      elif guess == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      else: 
        warnings -= 1
        if warnings == 0:
          print(f"Oops! That is not a valid input. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
          guesses -= 1
          warnings = 3
        else:
          give_warning(duplicate)
      
    if is_word_guessed(secret_word, letters_guessed):
      score = guesses*unique_letters(secret_word)
      print(f"Congratulations, you won!\nYour total score for this game is: {score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}")




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = "apples" # choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)


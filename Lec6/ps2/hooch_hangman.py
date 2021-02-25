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
    #turn secret word into list
    secret_word_list=list(secret_word)
    letters_guessed_check = []
    #make a list of only correctly guesed letters
    for i in range(len(letters_guessed)):
        for x in range(len(secret_word_list)):
            if letters_guessed[i] == secret_word_list[x]:
                letters_guessed_check.append(letters_guessed[i])

    #compare correct guessed letters to secret word as sets
    return set(letters_guessed_check) == set(secret_word_list)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    #turn secret word into list
    secret_word_list = list(secret_word)
    revealed_word_list = []
    for i in range(len(secret_word_list)):
        if str(secret_word_list[i]) in letters_guessed:
            revealed_word_list.append(secret_word_list[i])
        else:
            revealed_word_list.append("_")
    return ''.join(str(i) for i in revealed_word_list)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_list = list(alphabet)
    avaliable_letters = []
    for i in range(len(alphabet_list)):
        if alphabet_list[i] not in letters_guessed:
            avaliable_letters.append(alphabet_list[i])
    return ''.join(str(i) for i in avaliable_letters)
    
    

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

    secret_word_list = list(secret_word)
    secret_word_length = len(secret_word)
    letters_guessed = []
    guesses_left = 6
    warning = 3
    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {secret_word_length} letters long\n___")

    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left")
        print(f"Available letters {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter:")
        guess = guess.lower()  # force lowercase

        #check if user input is proper(a letter) WARNING
        while guess.isalpha() is False:
            warning -= 1
            print(f"Oops! That is not a valid letter. You have {warning} warnings left "
                  f"{get_guessed_word(secret_word, letters_guessed)}")
            if warning < 0:
                print("You Lose!")
                quit()
            guess = input("Please guess a letter:")
            guess = guess.lower()  # force lowercase

        #check if user has entered a previous guess WARNING
        if guess in letters_guessed:
            warning -= 1
            print(f"Oops! This letter has already been guessed. You have {warning} warnings left "
                  f"{get_guessed_word(secret_word, letters_guessed)}")
            if warning < 0:
                print("You Lose!")
                quit()
            guess = input("Please guess a letter:")
            guess = guess.lower()  # force lowercase
        letters_guessed.append(guess)

        #check if guess is in secret word
        if guess in secret_word_list:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}\n___")
        else:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}\n___")
            guesses_left -= 1
        #check if word is guessed
        if is_word_guessed(secret_word, letters_guessed) is True:
            print(f"Congratulations, you won!\nYour total score "
                  f"for this game is : {guesses_left * secret_word_length}\n___")
            quit()

    #Game is lost when you run out of guesses
    print(f"You have ran out of guesses.You are a loser. Better luck next time.\nThe answer was{secret_word}")

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

    my_word_list = list(my_word)
    other_word_list = list(other_word)
    check = True
    #check if each letter, that is not "_" matches
    for i in range(len(other_word_list)):
        if my_word_list[i] != other_word_list[i] and my_word_list[i] != "_":
            check *= False
    #check if there is an "_" where there would be a duplicate guessed letter
        if my_word_list[i] == "_":
            if other_word_list[i] in my_word_list:
                check *= False

    return bool(check)



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    my_word_list = list(my_word)
    temp = []

    for i in range(len(wordlist)):
        #add same word length and match with gaps to temp
        if len(my_word) ==len(wordlist[i]) and match_with_gaps(my_word,wordlist[i]):
            temp.append(wordlist[i])

    print(" ".join(temp))




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
      partially guesse word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    secret_word_list = list(secret_word)
    secret_word_length = len(secret_word)
    letters_guessed = []
    guesses_left = 6
    warning = 3
    vowel = ["a","e","i","o","u"]
    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {secret_word_length} letters long\n___")

    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left")
        print(f"Available letters {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter:")
        guess = guess.lower()  # force lowercase

        #allow user to gues a hint
        if guess == "*":
            print(f"Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
            print("---")
            continue

        #check if user input is proper(a letter) WARNING
        while guess.isalpha() is False and guess != "*":
            warning -= 1
            print(f"Oops! That is not a valid letter. You have {warning} warnings left "
                  f"{get_guessed_word(secret_word, letters_guessed)}")
            if warning < 0:
                print("You Lose!")
                quit()
            guess = input("Please guess a letter:")
            guess = guess.lower()  # force lowercase

        #check if user has entered a previous guess WARNING
        if guess in letters_guessed:
            warning -= 1
            print(f"Oops! This letter has already been guessed. You have {warning} warnings left "
                  f"{get_guessed_word(secret_word, letters_guessed)}")
            if warning < 0:
                print("You Lose!")
                quit()
            guess = input("Please guess a letter:")
            guess = guess.lower()  # force lowercase
        letters_guessed.append(guess)

        #check if guess is in secret word
        if guess in secret_word_list:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}\n___")
        elif guess in vowel:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}\n___")
            guesses_left -= 2
        else:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}\n___")
            guesses_left -= 1
        #check if word is guessed
        if is_word_guessed(secret_word, letters_guessed) is True:
            print(f"Congratulations, you won!\nYour total score "
                  f"for this game is : {guesses_left * secret_word_length}\n___")
            quit()

    #Game is lost when you run out of guesses
    print(f"You have ran out of guesses.You are a loser. Better luck next time.\nThe answer was {secret_word}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
   # secret_word = choose_word(wordlist)
   # hangman(secret_word)
    #my_word = "t__t"
    #other_word = "tadt"
   # show_possible_matches(my_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
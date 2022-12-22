'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from ntpath import join
from pickle import FALSE
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    1) word: str
        The word to be guessed picked randomly from the word_list.

    2) word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].

    3) num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet.

    4) num_lives: int
        The number of lives the player has.

    5) list_letters: list
        A list of the letters that have already been tried.

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list) #1 - Select one randomly from the word_list.
        self.word_guessed = list(('_')*int(len(self.word))) #2 - Mystery word with each letter replaced with '_', correct guessed word replace an '_'.
        self.num_letters = len(list(set(self.word))) #3 - UNIQUE number of letters in the mystery.
        self.num_lives= 5 #4 - Number of wrong guess permitted before player losses the game.
        self.list_letter = [] #5 -Place holder used to hold a list of the letters that have already been tried.
        self.num_char_in_word = len(self.word) #6 extra - Number of characters in mystery word.
        print(f'The mystery word has {len(self.word)} characters')
        print(f'{self.word_guessed}')
        print(f'You have {num_lives} lives.')
        # TODO 2a: Initialize the attributes as indicated in the docstring
        # TODO 2b: Print two message upon initialization:
        # DONE 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # DONE 2. {word_guessed}
        # J.P: added extra print to disply number of lives user has.
        pass
    
 
    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        self.letter = letter.lower()
        # self.start_index = self.word.find(self.letter) # needs changing
        # 1st check if letter is in word, if yes use  for loop to go through the whole word, if the word at that index number is equal to the letter.
       
        if self.letter in self.word:
            for p in range(0,len(self.word)):
               if self.word[p] == self.letter:
                    self.word_guessed[p] = self.letter
                    print('Weldone you guessed correctly')
                    print(f"Here is a hint to help guess the magic word'",''.join(self.word_guessed),"'. Please select another letter.")
                    print(f"You now have'",{self.num_lives},"' lives left. Please select another letter.")
                    self.list_letter.append(letter)
                    self.num_letters -= 1
                    self.turns = ''.join(self.word_guessed).count('_')
                    print(f"Number of turns = ",{self.turns})
        else:
            self.num_lives -= 1
            print(f"Sorry you letter '",{self.letter},"' is not part of the magic word.")
            print(f"You now have '",{self.num_lives},"' lives left.")
            self.list_letter.append(letter)
            self.turns = self.num_lives
        # print(f"Number of turns = ",{self.turns})
        # DONE TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # DONE TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # =>>>>>>>>> !!!! TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # =>>>>>>>>> !!!! Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        pass

    def ask_letter(self):

        i = self.num_lives
        while i > -1:
            print('Please type a letter')
            letter = input()
            if len(letter) != 1:
                print('Please, enter just one character')
            elif letter.isalpha() != True:
                print('Sorry your guess [ ',letter,' ] must be a one letter character')
            elif letter in self.list_letter:
                print(f"",{letter},"was already tried.")
            else:
                self.check_letter(letter)
                i = self.turns
            if i == 0:
                break
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # DONE TODO 1a: Ask the user for a letter iteratively until the user enters a valid letter [i.e. ask user for letter using a loop funcution]
        # DONE TODO 1b: Assign the letter to a variable called `letter`
        # TODO 1c: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2c: It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3c: If the letter is valid, call the check_letter method
        pass

# Play Game is a Function
# Hangman is a Class

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    if game.num_lives == 0:
        print(f"You ran out of lives. The word was {game.word}")
    else:
        #print("i'm there in the code -option 2-")
        print("Congratulations, you won!")
        print(f"The word was {game.word}")

    # DONE TODO 1d: To test this task, you can call the ask_letter method
    # TODO 2d: To test this task, upon initialization, two messages should be printed. 
    # TODO 3d: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    # word_list = ['apple']
    play_game(word_list)
# %%

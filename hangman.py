# Implementation of the game Hangman
import random
from words import words
import string

#this function will help in choosing a valid word without any "-" or " "
def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(word)
    return word.upper()

def hangman():
    word = get_valid_word(words)# it stores the guessed word
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase) # All the alphabets from A to Z
    used_letters = set() # letters guessed by the user
    lives = 7
    while len(word_letters) > 0 and lives > 0:
        
        print(f"You have {lives} lives left and you have used these letters",' '.join(used_letters))
        
        word_list=[]
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print("current word",' '.join(word_list))

        #user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("you lost 1 live")
        elif user_letter in used_letters:
            print(f"You have already guessed {user_letter}, try again")
        else:
            print("Invalid character!!!")

    #result 
    if lives == 0:
        print(f"You lost! current word was {word}")
    elif len(word_letters) == 0:
        print(f"Yah! You won! The word was {word}")

hangman()
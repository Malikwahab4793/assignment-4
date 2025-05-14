
import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print(f"You have used: {' '.join(used_letters)}")
        
        # Show current progress
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()

        if len(user_letter) == 1 and user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("Wrong letter.\n")
        elif len(user_letter) != 1:
            print("Please enter only ONE letter.\n")
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.\n")
        else:
            print("Invalid character. Please try again.\n")
    
    print(f"Congratulations! You guessed the word: {word}")

hangman()

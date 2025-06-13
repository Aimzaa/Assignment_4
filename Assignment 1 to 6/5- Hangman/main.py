import random

stages = ['''
    ----------
    |      |
    |
    |
    |
    |
    ----------
''',
'''
    --------
    |      |
    |      O
    |
    |
    |
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |      |
    |
    |
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|
    |
    |
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |
    |
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |     /
    |
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |     / \
    |
    --------
    ''']

words = ['apple', 'banana', 'kiwi', 'grapes', 'orange', 'mango', 'peach', 'plum', 'cherry']
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
guess_letters = []
lives = len(stages)-1
print("Welcome to Hangman! ")
print("Guess the fruits word. ")

while True:
    print(" ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) !=1:
        print("Invalid input. Please enter a single letter.\n ")
        continue

    if guess in guess_letters:
        print("You already guessed this letter. Try another one.\n ")
        continue

    guess_letters.append(guess)

    if guess in chosen_word:
        print(f"Good job! {guess} is in the word!")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        print(stages[len(stages) - lives -1])
        lives -= 1
        print(f"You have {lives} lives left.")

        if lives == 0:
            print(stages[lives])
            print(f"You lose! The word was '{chosen_word}'.")
            break


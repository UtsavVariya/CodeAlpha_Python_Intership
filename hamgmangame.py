import random

def hangman():
    word_list = ["monitor", "keyboard", "laptop", "mouse", "printer"]
    word_to_guess = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("_" * len(word_to_guess))

    while incorrect_guesses < max_incorrect:
        guess = input("Guess a Letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("please enter a single Letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word_to_guess:
            print("correct!")
        else:
            incorrect_guesses += 1
            print(f"incorrect! You have {max_incorrect - incorrect_guesses} guesses left.")

        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word.strip())

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word correctly!")
            break
    else:
        print(f"GFame over! The word was '{word_to_guess}'.")


hangman()


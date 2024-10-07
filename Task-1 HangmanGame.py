import random

# Default words
words = ["python", "javascript", "computer", "science", "programming", "algorithm", "database"]

def hangman():
    # Choose a random word from the list
    word = random.choice(words)
    word_length = len(word)
    display = ["_"] * word_length
    guessed_letters = []
    tries = 6

    print("Let's play Hangman!")
    print("You have", tries, "tries to guess the word.")

    stages = [  # Stages built progressively
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    while "_" in display and tries > 0:
        print(stages[6-tries])
        print(" ".join(display))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please guess a single letter.")
        elif guess in guessed_letters:
            print("You already guessed this letter.")
        elif guess not in word:
            print("This letter is not in the word.")
            tries -= 1
            guessed_letters.append(guess)
        else:
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
            guessed_letters.append(guess)

        print("Tries remaining:", tries)

    print(stages[6-tries])
    if "_" not in display:
        print(" ".join(display))
        print("Congratulations, you won! The word was", word)
    else:
        print("Game over. The word was", word)

def main():
    play_again = "y"
    while play_again.lower() == "y":
        hangman()
        play_again = input("Do you want to play again? (y/n): ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
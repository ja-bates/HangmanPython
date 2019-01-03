import random


# Allows user to input name and provides game instructions
def welcomeScreen():
    name = input("Enter Your Name:")
    print("Welcome, " + str(name) + ", to a friendly game of Hangman!")
    print("Try to complete the word by guessing letters. (LOWERCASE LETTERS ONLY)")
    print("You have 9 lives (wrong guesses)")
    print("Ready...")
    print("Set...")
    print("GO!")
    print()
    main()
    print()


def main():
    # Randomly selecting the word
    word = random.choice(["programming", "python", "pony", "knight", "castle"])
    # Giving the user a hint as to what the word is
    if word == "castle":
        print("HINT: chess")
    if word == "knight":
        print("HINT: chess")
    if word == "pony":
        print("HINT: animal")
    if word == "python":
        print("HINT: programming")
    if word == "programming":
        print("HINT: python")
    # Defining what letters the user is allowed to guess
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessed = ''

    # Make sure we have a word
    while len(word) > 0:
        msg = ""

        # Check if the letter is in the random word
        for letter in word:
            if letter in guessed:
                # If the letter is in the word then print it in that spot
                msg = msg + letter
            else:
                # Otherwise, print a blank
                msg = msg + "_" + " "

        # When all the letters are filled in, tell the user they are correct
        if msg == word:
            print(str(msg))
            print("CORRECT! The word was " + str(word))
            break

        # setting up the guessing interface
        print("Guess the Word: ", str(msg))
        guess = input()

        # Recognizes if the guess is valid or not
        if guess in validLetters:
            guessed = guessed + guess

        else:
            print("Invalid Entry. Enter a Valid Lowercase Letter to continue:")
            guess = input()
            # Allows program to recognize a correct guess after a invalid input
            if guess in validLetters:
                guessed = guessed + guess

        # Keeps track of the Lives and prints the Hangman
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("Nice try but nope. Lives Remaining: 8")
                print(" o")
            if turns == 8:
                print("Nice try but nope. Lives Remaining: 7")
                print(" o")
                print(" |")
            if turns == 7:
                print("Nice try but nope. Lives Remaining: 6")
                print(" o")
                print(" |")
                print(" /")
            if turns == 6:
                print("Nice try but nope. Lives Remaining: 5")
                print(" o")
                print(" |")
                print("/ \ ")
            if turns == 5:
                print("Nice try but nope. Lives Remaining: 4")
                print(" o")
                print(" |-")
                print("/ \ ")
            if turns == 4:
                print("Nice try but nope. Lives Remaining: 3")
                print(" o")
                print("-|-")
                print("/ \ ")
            if turns == 3:
                print("Nice try but nope. Lives Remaining: 2")
                print("  o")
                print(" -|-")
                print("_/ \ ")
            if turns == 2:
                print("Nice try but nope. Lives Remaining: 1")
                print("  o")
                print(" -|-")
                print("_/ \_")
            if turns == 1:
                print("YOU LOSE!! The word: " + str(word) + " :was just too advanced for you :-) ")
                break


welcomeScreen()











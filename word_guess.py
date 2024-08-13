import random

title = "Guess The Word Challenge!"

word_bank = ["black","brown","white","green","hazel","olive","peach"]

a=[]

for i in word_bank:
        a.append(i.rstrip().lower())

word_to_guess = random.choice(a)

#Defining game variables
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

while True:

    #Current state of the game
    print("--------------------","Welcome to", title,"----------------------")
    print("The word has", len(word_to_guess), "letters.")
    print("You have", max_turns - turns_taken, "turns left.")

    while turns_taken < max_turns:

        guess = input("Guess a word: ").lower()

    
        if len(guess) != len(word_to_guess) or not guess.isalpha():
            print("Please enter 5-letter word.")
            continue

        # To check each letter in the guess compared to the word's letters
        index = 0
        for c in guess:
            if c == word_to_guess[index]:
                print(c, end=" ")
                if c in misplaced_guesses:
                    misplaced_guesses.remove(c)
            elif c in word_to_guess:
                if c not in misplaced_guesses:
                    misplaced_guesses.ap0pend(c)
                print("_", end=" ")
            else:
                if c not in incorrect_guesses:
                    incorrect_guesses.append(c)
                print("_", end=" ")
            index += 1

        print("\n")
        print("Misplaced letters: ", misplaced_guesses)
        print("Incorrect letters: ", incorrect_guesses)
        turns_taken += 1


        

        # To check if the player has won
        if guess == word_to_guess:
            print("Congratulations, you win!")
            play = input("Would you like to play again?(y/n):")
            if play == "y":
                break
            else:
                quit()

        # To check if the player has lost
        if turns_taken == max_turns:
            print("Sorry, you lost. The word was", word_to_guess)
            reset = input("Would you like to play again?(y/n):")
            if reset == "n":
                quit()
        

        # To display the number of turns left
        print("You have", max_turns - turns_taken, "turns left.")
        

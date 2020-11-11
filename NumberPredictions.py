import random

DiceNumber = int("0") #=- The number the dice rolls. -=#

Tries = int("0") #=- Amount of attempts. -=#

PlayerNumber = int("0") #=- Player's Number. -=#

while True:
    DiceNumber = int(random.randint(1, 6)) #=- Randomizes the dice number each time. -=#

    Tries += 1 #=- For every time he incorrectly guesses, it adds another to the amount of times he had attempted. -=#

    PlayerNumber = int(input("Predict the number. ")) #=- Asks for the number he predicts -=#

    if PlayerNumber == DiceNumber: #=- If he is correct, the game ends. -=#
        print("You guessed the correct number.")
        print("It took you", Tries, "tries before you were correct.")
        break

    if PlayerNumber >= DiceNumber: #=- If the number he guessed is bigger than the dice's number, he loses -=#
        print("You guessed a number bigger than the roll.")

    if PlayerNumber <= DiceNumber: #=- If the number he guessed is smaller than the dice's number, he loses -=#
        print("You guessed a number smaller than the roll.")
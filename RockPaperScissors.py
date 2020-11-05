import random 

PlayerChoice = str(input("Please select a character.(Vader, Yoda, or Obi-Wan). ")) #Setting the player's word choice.

ComputerNumber = int(random.randint(1, 3)) #Setting the computer's choice randomly. 

PlayerNumber = 1

#==| Converting Player's Choice into a number |==#

if PlayerChoice == "Yoda":
    PlayerNumber == 2

if PlayerChoice == "Obi-Wan":
    PlayerNumber == 3

if PlayerChoice == "Vader":
    PlayerNumber == 1

#==| Deciding who wins |==#

if PlayerNumber == ComputerNumber: 
    print("It was a tie!")

if PlayerNumber  == 1 and ComputerNumber == 2:
    print("Yoda beat Vader.")

if PlayerNumber  == 1 and ComputerNumber == 3: 
    print("Vader beat Obi-Wan")

if PlayerNumber  == 2 and ComputerNumber == 1: 
    print("Yoda beat Vader.")

if PlayerNumber  == 2 and ComputerNumber == 3: 
    print("Obi-Wan beat Yoda.")

if PlayerNumber  == 3 and ComputerNumber == 1:
    print("Vader beat Obi-Wan")

if PlayerNumber  == 3 and ComputerNumber == 2: 
    print("Obi-Wan beat Yoda.")
    
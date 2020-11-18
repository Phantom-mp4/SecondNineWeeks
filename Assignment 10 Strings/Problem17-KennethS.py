Word = input("Please input a word. ")

WordLength = len(Word) #Finds length of the inputed word.

EPos =  Word.find("e")

LetterOn = 0

while LetterOn <= WordLength:
    print(EPos, Word[EPos])
    break

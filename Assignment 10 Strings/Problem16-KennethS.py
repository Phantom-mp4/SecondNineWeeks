Word = input("Please input a word. ")

WordLength = len(Word) #Finds length of the inputed word.

WordStart = 0


while WordStart <= WordLength:
    print(Word[::-1]) 
    break

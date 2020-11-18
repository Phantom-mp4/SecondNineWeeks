Word = input("Enter a word. ")

WordLength = len(Word)

if WordLength <= 2:
    print(Word)

WordTwo = Word[0:2]

print(Word[2:WordLength], WordTwo)

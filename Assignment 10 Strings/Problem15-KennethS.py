Word = input("Enter a word. ")

WordLength = len(Word)

WordStart = 0

while WordStart <= WordLength:
    if WordStart % 2 == 0:
        print(Word[WordStart])
    WordStart += 1 

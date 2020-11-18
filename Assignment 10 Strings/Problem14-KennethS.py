Word = input("Enter a word. ")

WordLength = len(Word)

WordStart = 0

while WordStart <= WordLength:
    print(Word[WordStart])
    WordStart += 1
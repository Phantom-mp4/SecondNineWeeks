Word = input("Please input a word. ")

BackwardsWord = Word[::-1]

if Word == BackwardsWord:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
Word = input("Please input a word. ")

WordLength = len(Word) #Finds length of the inputed word.
WordHalfLength = WordLength // 2 #Cuts the length in 2 and making it into a whole number.

WordFirstHalf = Word[0:WordHalfLength] #Sets it to where the beginning starts, and the half way point.
WordSecondHalf = Word[WordHalfLength:WordLength] #Sets it to where the Half ends, to the end of the string.

print(WordFirstHalf[::-1]) 
print(WordSecondHalf[::-1])

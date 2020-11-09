InputNumber = int(input("Give me a number. "))

if InputNumber <= 0:
        print(InputNumber, "is below 0")

while InputNumber >= 0:

    if InputNumber % 2 == 0:
        print(InputNumber, "Is even.")
        InputNumber = int(input("Give me a number. "))

    if InputNumber % 2 == 1:
            print(InputNumber, "Is odd.")
            InputNumber = int(input("Give me a number. "))
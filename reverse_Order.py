def reverse_Order_Number(arrange):
    for number1 in range(len(arrange)):
        for number2 in range(number1 + 1, len(arrange)):
            if arrange[number1] > arrange[number2]:
                arrange[number1], arrange[number2] = arrange[number2], arrange[number1]
    return arrange


def maintain_Order_Number(arrange):
    for number1 in range(len(arrange)):
        for number2 in range(number1 + 1, len(arrange)):
            if arrange[number1] < arrange[number2]:
                arrange[number1], arrange[number2] = arrange[number2], arrange[number1]
    return arrange


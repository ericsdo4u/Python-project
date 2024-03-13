# count_input = input("Enter input to count")

count_input = "hello word!, 123"


def count_word(count_sentence):
    numbers = 0
    letters = 0
    for item in count_sentence:
        if item.isalpha():
            letters += 1
        if item.isdigit():
            numbers += 1

    return f'("NUMBERS" {numbers} "LETTERS", {letters})'


print(count_word(count_input))

count_input_two = "hEllo worLD"


def count_upper_lower(word):
    upper_letters = 0
    lower_letters = 0
    for items in word:
        if items.isupper():
            upper_letters += 1
        if items.islower():
            lower_letters += 1

    return f'("UPPER_LETTERS" {upper_letters} "LOWER_LETTERS" {lower_letters})'


print(count_upper_lower(count_input_two))

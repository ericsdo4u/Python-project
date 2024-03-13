sample_List = []
for num in range(10, 20):
    sample_List.append(num)


def get_Length_Of_List(sample_List):
    count = 0
    for num in sample_List:
        count += num
        return count


def sum_All_Elemet_Of_Even(sample_List):
    sums = 0
    for num in sample_List:
        if num % 2 == 0:
            sums += num
    return sums


def sum_Odd_Element(sample_list):
    sums = 0
    for num in sample_list:
        if num % 2 == 1:
            sums += num
    return sums


def multiply_Element_In_Third_Position(sample_list):
    product = 1
    for num in range(2, len(sample_list), 3):
        product = sample_list[3] * 3
    return product


def average_Element_in_list(sample_list):
    average = 0
    total = 0
    for num in sample_list:
        total += num
    average = total / num
    return average


def largest_Element(sample_list):
    largest = sample_list[0]
    for num in sample_list:
        if num > largest:
            largest = num
    return largest


def smallest_Element(sample_list):
    smallest = sample_list[0]
    for num in sample_list:
        if num < smallest:
            smallest = num
    return smallest


def get_String_If_First_And_Last_Word_Is_Equal(words):
    result = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            result.append(word)
        return result


def count_word(text):
    #     word_count = {}
    #     for word in text.split():
    #         if word in text:
    #             word_count[word] += 1
    #         else:
    #             word_count[word] = 1
    from collections import Counter
    Counter = Counter(text.split())
    for word, count in sorted(Counter.items()):
        return len(Counter)

    # even_number = 0
    # odd_number = 0
    # try:
    #     numbers = int(input("Enter numbers :"))
    # except ValueError:
    #     print('invalid input')
    #     for number in range(1,numbers):
    #         if number % 2 == 0:
    #             even_number += number
    #         else:
    #             odd_number += number
    # print(even_number, odd_number)


def sum_even_and_odd_numbers(numbers):
    try:
        # numbers = int(input("Enter numbers :"))
        sum_even = sum(list(range(1, numbers))[1::2])
        sum_odd = sum(list(range(1, numbers))[::2])
        return sum_even, sum_odd
    except ValueError:
        print("Invalid")




def sum_collection(element):
    number = set(element)
    return sum(number)


def swap_string(input1, input2):
    return input2[0:2] + input1[2::] + " " + input1[0:2] + input2[2::]


def add_numbers_to_set(user_input):
    list_of_numbers = set()
    for number in user_input:
        list_of_numbers.add(number)
    return list_of_numbers


def remove_number(element):
    lst_of_set = set()
    for number in element:
        lst_of_set.add(number)
        if number == 3:
            lst_of_set.discard(number)
    return lst_of_set





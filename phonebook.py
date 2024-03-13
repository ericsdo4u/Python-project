numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_odd(number):
    return number % 2 != 0

num = [item for item in numbers if is_odd(item)]
print(num)

#print(list(filter(is_odd, numbers)))

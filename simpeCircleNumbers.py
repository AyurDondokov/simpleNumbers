
def is_simple(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def all_other_numbers(number):
    result = []
    array_of_numbers = str(number)
    for i in range(len(array_of_numbers)):
        result.append(int(array_of_numbers[-(i+1):len(array_of_numbers)] + array_of_numbers[0:-(i+1)]))
    return result[:-1]


def is_circle_simple(number):
    for i in all_other_numbers(number):
        if not is_simple(i):
            return False
    return True


n = 1000000
a = [i for i in range(n + 1)]

list_circle_numbers = []
counter = 0

for i in range(1, n):
    if is_simple(a[i]) and is_circle_simple(a[i]):
        list_circle_numbers.append(a[i])
        counter += 1

print(f"Все круговые числа:\n{list_circle_numbers}")
print(f"Количество простых круговых чисел: {counter}")

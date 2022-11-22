import itertools

def is_simple(number):
    if number == 2 or number == 3: return True
    if number % 2 == 0 or number < 2: return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def all_other_numbers(number):
    result = []
    a = str(number)
    for i in range(len(a)):
        result.append(int(a[-(i+1):len(a)] + a[0:-(i+1)]))
    return result[:-1]

def is_circle_simple(number):
    for i in all_other_numbers(number):
        if is_simple(i) == False:
            return False
    return True
n = 1000000
a = [i for i in range(n + 1)]
print(a)

counter = 0

for i in range(n):
    if a[i] != 0 and is_simple(a[i]) and is_circle_simple(a[i]):
        counter += 1

print(counter)
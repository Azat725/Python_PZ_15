import random
from random import randint

my_list = [randint(-100, 100) for _ in range(6)]

print(my_list)
print()

even_numbers_list = []
odd_numbers_list = []
negative_numbers_list = []
positive_numbers_list = []

#список содержащий только четные числа
for even_numbers in my_list:
    if even_numbers % 2 == 0:
        even_numbers_list.append(even_numbers)

print(even_numbers_list)
print()

#список содержащий только нечетные числа
for odd_numbers in my_list:
    if odd_numbers % 2 != 0:
        odd_numbers_list.append(odd_numbers)

print(odd_numbers_list)
print()

#список содержащий только отрицательные числа
for negative_numbers in my_list:
    if negative_numbers < 0:
        negative_numbers_list.append(negative_numbers)
        
print(negative_numbers_list)
print()

#список содержащий только положительные числа
for positive_numbers in my_list:
    if positive_numbers > 0:
        positive_numbers_list.append(positive_numbers)
        
print(positive_numbers_list)
print()

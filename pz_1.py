#В списке целых, заполненном случайными числами вычислить:
#Сумму отрицательных чисел
#Сумму четных чисел
#Сумму нечетных чисел
#Произведение элементов с индексами кратными 3
#Произведение элементов между минимальным и максимальным элементом
#Сумму элементов, находящихся между первым и последним положительными элементами

import functools
import random
from random import randint

my_list = [randint(-100, 100) for _ in range(5)]
print(my_list)
print()

negative_list = [] #массив отрицательных чисел
even_list = [] #массив четных чисел
not_even_list = [] #массив нечетных чисел
is_multiple_three_list = []
result = 1


#сумма отрицательных чисел
for negative_numbers in my_list:
    if negative_numbers < 0:
        negative_list.append(negative_numbers)
    else:
        None
        
print(negative_list)
print(f"Сумма отрицательных чисел = {sum(negative_list)}")
print()

#Сумма четных чисел
for even_numbers in my_list:
    if even_numbers % 2 == 0:
        even_list.append(even_numbers)
    else:
        None
        
print(even_list)
print(f"Сумма четных чисел = {sum(even_list)}")
print()

#Сумма нечетных чисел
for not_even_numbers in my_list:
    if not_even_numbers % 2 != 0:
        not_even_list.append(not_even_numbers)
    else:
        None
        
print(not_even_list)
print(f"Сумма нечетных чисел = {sum(not_even_list)}")
print()

#Произведение элементов с индексами кратными 3
for is_multiple_three_numbers in my_list:
    if is_multiple_three_numbers % 3 == 0:
        is_multiple_three_list.append(is_multiple_three_numbers)
    else:
        None
        
for mul_is_multiple_list in is_multiple_three_list:
    result *= mul_is_multiple_list
        
print(is_multiple_three_list)
print(f"Произведение чисел, кратных '3' = {result}")
print()

#Произведение элементов между минимальным и максимальным элементом
min_index = my_list.index(min(my_list))
max_index = my_list.index(max(my_list))

if min_index < max_index:
    result_min_max = 1
    for mul_min_max in range(min_index + 1, max_index):
        result_min_max *= my_list[mul_min_max]
        
    print(max(my_list))
    print(min(my_list))
    print(f"Произведение элементов между минимальным и максимальным элементом = {result_min_max}")
    print()

else:
    result_min_max = 1
    for mul_min_max in range(max_index + 1, min_index):
        result_min_max *= my_list[mul_min_max]
        
    print(max(my_list))
    print(min(my_list))
    print(f"Произведение элементов между минимальным и максимальным элементом = {result_min_max}")
    print()
    
#Сумма элементов, находящихся между первым и последним положительными элементами
element_incides = [i for i, x in enumerate(my_list) if x > 0]
if len(element_incides) >= 2:
    first_element = element_incides[0]
    last_element = element_incides[-1]
    if first_element > last_element:
        sum_between_elements = sum(my_list[first_element + 1 : last_element])
    else:
        sum_between_elements = sum(my_list[last_element + 1 : first_element])
        
print(sum_between_elements)
print()
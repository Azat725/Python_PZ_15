import random
from random import randint

my_list = [randint(1, 10) for _ in range(10)] 

print(my_list)

for i in my_list:
    print(f"element: {i}")
    
for i in range(len(my_list)):
    print(f"index: {i}")
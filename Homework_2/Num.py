# Номер 1

# number = (input())
# summ = 0
# for symbol in number:
#     if symbol.isdigit():
#         summ += int(symbol)
# print(summ)



# Номер 2

# n = int(input())
# some_list =[1]
# fact = 1
# for i in range(2, n + 1):
#     fact *= i 
#     some_list.append(fact)
# print(some_list)



# Задачаа 3

# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += (1 + 1 / i) ** i
# print(summ)



# Задача 5

import random # Подключение библиотеки random
some_list = []
for _ in range(10):
    some_list.append(random.randint(0, 10))
print(f'Начальный список: {some_list}')
random.shuffle(some_list)
print(f'Перемешанный список: {some_list}')
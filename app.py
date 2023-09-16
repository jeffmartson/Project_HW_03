import numpy as np

# Ввод последовательности чисел
input_str = input("Введите последовательность чисел через пробел: ")
try:
    numbers = np.array([int(num) for num in input_str.split()])
except ValueError:
    print("Ошибка: Введите только числа через пробел.")
    exit(1)

# Ввод числа пользователя
user_number = int(input("Введите число: "))

# Сортировка
sorted_numbers = np.sort(numbers)

# Поиска позиции числа в отсортированном массиве с помощью метода searchsorted
position = np.searchsorted(sorted_numbers, user_number)

# Проверка на наличие числа в массиве
if position < len(sorted_numbers):
    print(f"Ближайшее число, меньшее {user_number}, "
          f"находится на позиции {position} и равно {sorted_numbers[position]}.")
    print(f"Следующее число, большее или равное {user_number}, "
          f"находится на позиции {position + 1} и равно {sorted_numbers[position + 1]}.")
else:
    print(f"В последовательности нет чисел меньших {user_number}.")

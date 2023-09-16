# Project_HW_03

# Программа для поиска ближайших чисел

Простая Python-программа, которая позволяет находить ближайшие числа в заданной последовательности.

## Описание

Эта программа принимает последовательность чисел от пользователя через пробел, а также запрашивает у пользователя число. Затем она выполняет следующие действия:

1. Преобразование введённой последовательности в список чисел.

2. Сортировка списка по возрастанию.

3. Поиск числа, которое меньше введенного пользователем числа, а следующего за ним больше или равен этому числу с использованием алгоритма двоичного поиска.

При нахождении ближайших чисел программа выводит информацию о них, а если таких чисел нет, она сообщает об этом.

## Требования

Для запуска программы вам понадобится Python версии 3.x.

## Установка и запуск

1. Склонируйте репозиторий или скачайте файлы программы на свой компьютер.

2. Откройте командную строку (терминал) и перейдите в каталог с файлами программы.

3. Запустите программу, выполните следующую команду:

   ```shell
   python app.py

Следуйте инструкциям в программе.

Пример использования:

Введите последовательность чисел через пробел: 5 10 15 20 25
Введите число: 12
Ближайшее число, меньшее 12, находится на позиции 1 и равно 10.
Следующее число, большее или равное 12, находится на позиции 2 и равно 15.
